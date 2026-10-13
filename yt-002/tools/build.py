#!/usr/bin/env python3
"""YT-002 build pipeline.

data/shots.json を唯一の正とし、以下を生成する。

  python3 tools/build.py check    -> 尺・字幕タイミングの検査のみ
  python3 tools/build.py docs     -> subtitles/YT-002.srt, subtitles/YT-002.ass, prompts/02_prompts.md, docs/01_script.md
  python3 tools/build.py render   -> output/*.mp4

render は clips/<ショットID>.(mp4|mov|webm) があればその映像を使い、
無いショットは「仮映像カード」で埋める。1つでも仮映像が残っていれば
出力名は animatic_YT-002.mp4 になり、完成版 (YT-002_final.mp4) とは区別される。
効果音は audio/<key>.(wav|mp3|flac|ogg) があればそれを使い、無ければ
仮のシンセ音（またはBGMなら無音）で代用する。
"""
import json
import math
import os
import shutil
import subprocess
import sys
import textwrap

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "shots.json")
SR = 48000

FONT_FILE = os.environ.get("FONT_FILE", "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf")
FONT_NAME = os.environ.get("FONT_NAME", "IPAGothic")


def load():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- subtitles

def ts_srt(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def ts_ass(t):
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"


def write_srt(d, path):
    # SRT は YouTube の字幕(CC)用。演出用テロップ(Comic/Aside)も意味が通るよう含める。
    events = []
    for shot in d["shots"]:
        for s in shot["subs"]:
            events.append((s["start"], s["end"], s["text"].replace("\\N", "\n")))
    events.sort()
    with open(path, "w", encoding="utf-8") as f:
        for i, (a, b, text) in enumerate(events, 1):
            f.write(f"{i}\n{ts_srt(a)} --> {ts_srt(b)}\n{text}\n\n")


# ASS colours are &HAABBGGRR
ASS_STYLES = [
    # name, size, primary, outline, back, bold, borderstyle, outline_w, shadow, align, marginL, marginR, marginV
    ("Shiro",   62, "&H00FFFFFF", "&H00000000", "&H80000000", -1, 1, 4, 2, 2, 80, 80, 70),
    ("Tora",    62, "&H007AC2FF", "&H00000000", "&H80000000", -1, 1, 4, 2, 2, 80, 80, 70),
    ("Mike",    62, "&H008AF0D8", "&H00000000", "&H80000000", -1, 1, 4, 2, 2, 80, 80, 70),
    ("Narr",    52, "&H00FFFFFF", "&H90000000", "&H90000000", 0, 3, 14, 0, 2, 80, 80, 70),
    ("Caption", 56, "&H00000000", "&H0000D7FF", "&H0000D7FF", -1, 3, 14, 0, 8, 80, 80, 60),
    ("Comic",  110, "&H0000E6FF", "&H00000000", "&H00000000", -1, 1, 7, 3, 8, 80, 80, 170),
    ("Aside",   46, "&H00FFFFFF", "&H00000000", "&H80000000", -1, 1, 3, 1, 9, 60, 60, 120),
    ("Title",  112, "&H00FFFFFF", "&H00000000", "&HA0000000", -1, 1, 6, 4, 5, 80, 80, 0),
    ("CardQ",   76, "&H00FFFFFF", "&H00000000", "&H00000000", -1, 1, 0, 0, 5, 120, 120, 0),
    ("CardSub", 50, "&H00FFD09F", "&H00000000", "&H00000000", 0, 1, 0, 0, 2, 120, 120, 250),
    ("Notice",  34, "&H00FFFFFF", "&H90000000", "&H90000000", 0, 3, 10, 0, 2, 60, 60, 96),
    ("Label",   32, "&H30FFFFFF", "&HA0000000", "&HA0000000", -1, 3, 8, 0, 7, 36, 36, 30),
    ("OSD",     36, "&H20FFFFFF", "&H00000000", "&H00000000", 0, 1, 2, 0, 1, 36, 36, 26),
]

ASS_FX = {
    "Title": r"{\fad(250,300)}",
    "Comic": r"{\fscx135\fscy135\t(0,120,\fscx100\fscy100)\fad(0,150)}",
    "Caption": r"{\fad(120,120)}",
    "CardQ": r"{\fad(300,200)}",
    "CardSub": r"{\fad(300,200)}",
}


def write_ass(d, path):
    w, h = d["resolution"]
    out = [
        "[Script Info]",
        f"Title: {d['project']} {d['title']}",
        "ScriptType: v4.00+",
        f"PlayResX: {w}",
        f"PlayResY: {h}",
        "WrapStyle: 0",
        "ScaledBorderAndShadow: yes",
        "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
        "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
    ]
    for (name, size, pri, outl, back, bold, bs, ow, sh, al, ml, mr, mv) in ASS_STYLES:
        out.append(f"Style: {name},{FONT_NAME},{size},{pri},&H000000FF,{outl},{back},{bold},0,0,0,100,100,0,0,{bs},{ow},{sh},{al},{ml},{mr},{mv},1")
    out += ["", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]

    total = d["shots"][-1]["end"]
    out.append(f"Dialogue: 5,{ts_ass(0)},{ts_ass(total)},Label,,0,0,0,,{d['label']}")

    for shot in d["shots"]:
        osd = shot.get("osd")
        if osd:
            # 防犯カメラ風のOSD。秒が進むように1秒ごとにイベントを切る。
            date, clock = osd["datetime"].split(" ")
            hh, mm, ss = (int(x) for x in clock.split(":"))
            base = hh * 3600 + mm * 60 + ss
            t = shot["start"]
            k = 0
            while t < shot["end"] - 1e-6:
                t2 = min(shot["start"] + k + 1, shot["end"])
                sec = base + k
                stamp = f"{date} {sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"
                out.append(f"Dialogue: 4,{ts_ass(t)},{ts_ass(t2)},OSD,,0,0,0,,● REC  {osd['cam']}   {stamp}")
                t = t2
                k += 1
        for s in shot["subs"]:
            fx = ASS_FX.get(s["style"], r"{\fad(80,80)}")
            out.append(f"Dialogue: 10,{ts_ass(s['start'])},{ts_ass(s['end'])},{s['style']},,0,0,0,,{fx}{s['text']}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


# ------------------------------------------------------------------ prompts

def full_prompt(d, shot):
    p = shot["prompt"]
    for k, v in d["characters"].items():
        name, desc = v.split(": ", 1)
        p = p.replace("{" + k + "}", f"{name} ({desc})")
    return f"{d['cameras'][shot['camera']]}. {p} {d['style_suffix']}."


def write_prompts(d, path):
    lines = [
        f"# {d['project']} 映像生成プロンプト（自動生成）",
        "",
        "> このファイルは `tools/build.py docs` が `data/shots.json` から生成します。編集は shots.json 側で行ってください。",
        "",
        "## 共通ネガティブプロンプト",
        "",
        "```",
        d["negative"],
        "```",
        "",
        "## キャラクター記述ブロック（全プロンプトに一字一句同じ文を埋め込む）",
        "",
    ]
    for k, v in d["characters"].items():
        lines += [f"- **{k}**: `{v}`"]
    lines += ["", "## ショット別", ""]
    for shot in d["shots"]:
        dur = shot["end"] - shot["start"]
        lines.append(f"### {shot['id']}（{shot['start']:.1f}–{shot['end']:.1f}s / {dur:.1f}秒 / {shot['camera']}）")
        lines.append("")
        lines.append(f"- 内容: {shot['action_ja']}")
        if shot["camera"] == "CARD":
            lines += ["- 生成不要（編集でテキストカードを作成）", ""]
            continue
        refs = ", ".join(f"refs/{c.lower()}_*.png" for c in shot["cats"])
        lines.append(f"- 参照画像: {refs}")
        lines.append(f"- 生成尺: 5秒で生成 → 編集で {dur:.1f} 秒にトリム")
        lines += ["", "```", full_prompt(d, shot), "```", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


SCENES = {
    1: "導入：妻猫、玄関に現る（0〜12秒）",
    2: "回想：仲良く過ごす二匹（12〜27秒）",
    3: "隠されたスマホ（27〜42秒）",
    4: "妻猫の登場、発覚（42〜57秒）",
    5: "三匹の対峙（57〜72秒）",
    6: "問いかけ（72〜90秒）",
}


def write_script(d, path):
    lines = [
        f"# {d['project']}『{d['title']}』シーン別台本（自動生成）",
        "",
        "> `tools/build.py docs` が `data/shots.json` から生成。人間のナレーションなし。セリフはすべて字幕、猫は口パクしない。",
        f"> 全編左上に「{d['label']}」ラベルを常時表示。",
        "",
    ]
    for sc, title in SCENES.items():
        lines += [f"## シーン{sc}　{title}", "", "| ショット | 時間 | カメラ | 映像 | 字幕・テロップ | 音 |", "|---|---|---|---|---|---|"]
        for shot in (s for s in d["shots"] if s["scene"] == sc):
            subs = "<br>".join(f"[{s['style']}] {s['text'].replace(chr(92) + 'N', ' ')}" for s in shot["subs"]) or "—"
            sfx = "<br>".join(f"{c['t']:.1f}s {c['key']}" for c in shot["sfx"]) or "—"
            lines.append(f"| {shot['id']} | {shot['start']:.1f}–{shot['end']:.1f} | {shot['camera']} | {shot['action_ja']} | {subs} | {sfx} |")
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# -------------------------------------------------------------------- audio

def env_decay(n, tau):
    return np.exp(-np.arange(n) / (tau * SR))


def lowpass(x, k):
    if k <= 1:
        return x
    return np.convolve(x, np.ones(k) / k, mode="same")


def tone(freq, dur, tau, harmonics=(1.0, 0.3, 0.1)):
    n = int(dur * SR)
    t = np.arange(n) / SR
    y = sum(a * np.sin(2 * np.pi * freq * (i + 1) * t) for i, a in enumerate(harmonics))
    return y * env_decay(n, tau)


def sweep(f0, f1, dur, vib=0.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = np.interp(t, [0, dur], [f0, f1]) + vib * np.sin(2 * np.pi * 6 * t)
    ph = 2 * np.pi * np.cumsum(f) / SR
    y = np.sin(ph) + 0.35 * np.sin(2 * ph) + 0.15 * np.sin(3 * ph)
    return y * np.sin(np.pi * t / dur) ** 0.6


rng = np.random.default_rng(2)


def noise(n):
    return rng.standard_normal(n)


def synth(key, dur):
    """仮効果音。本番では audio/<key>.wav を置いて差し替える。"""
    if key == "doorbell":
        return np.concatenate([tone(659, 0.45, 0.35), tone(523, 1.1, 0.5)]) * 0.5
    if key in ("phone_vibrate", "phone_vibrate_muffled"):
        n = int(dur * SR)
        t = np.arange(n) / SR
        f = 150 if key == "phone_vibrate" else 110
        buzz = np.sign(np.sin(2 * np.pi * f * t)) * 0.6 + noise(n) * 0.15
        gate = ((t % 0.65) < 0.4).astype(float)
        y = lowpass(buzz * gate, 8 if key == "phone_vibrate" else 40)
        return y * 0.6
    if key == "title_hit":
        n = int(1.8 * SR)
        t = np.arange(n) / SR
        boom = np.sin(2 * np.pi * (70 - 30 * t / 1.8) * t) * env_decay(n, 0.5)
        return boom + lowpass(noise(n), 30) * env_decay(n, 0.08) * 0.8
    if key == "tension_hit_small":
        return tone(82, 0.8, 0.25, (1.0, 0.5)) * 0.8
    if key == "comic_slap":
        n = int(0.12 * SR)
        return np.diff(noise(n + 1)) * env_decay(n, 0.018) * 0.5
    if key == "comic_pluck":
        return np.concatenate([tone(988, 0.12, 0.04), tone(784, 0.3, 0.06)]) * 0.5
    if key == "cat_flap":
        n = int(0.25 * SR)
        y = lowpass(noise(n), 6) * env_decay(n, 0.01)
        y[int(0.12 * SR):] += lowpass(noise(n - int(0.12 * SR)), 6) * env_decay(n - int(0.12 * SR), 0.01) * 0.6
        return y
    if key == "purr":
        n = int(dur * SR)
        t = np.arange(n) / SR
        am = 0.5 + 0.5 * np.sin(2 * np.pi * 26 * t)
        y = lowpass(noise(n), 120) * am * 4
        fade = np.minimum(1, np.minimum(t / 0.3, (dur - t) / 0.3))
        return y * fade
    if key == "eating":
        n = int(dur * SR)
        y = np.zeros(n)
        for p in rng.uniform(0, dur - 0.05, int(dur * 6)):
            i = int(p * SR)
            m = int(0.04 * SR)
            y[i:i + m] += noise(m) * env_decay(m, 0.008) * 0.4
        return y
    if key == "paw_scramble":
        n = int(dur * SR)
        y = np.zeros(n)
        for p in rng.uniform(0, dur - 0.03, int(dur * 25)):
            i = int(p * SR)
            m = int(0.02 * SR)
            y[i:i + m] += lowpass(noise(m), 3) * env_decay(m, 0.004) * 0.6
        return y
    if key == "box_thud":
        return tone(120, 0.3, 0.06, (1.0, 0.2)) * 0.9
    if key == "drone_question":
        n = int(dur * SR)
        t = np.arange(n) / SR
        y = (np.sin(2 * np.pi * 110 * t) + 0.6 * np.sin(2 * np.pi * 164.8 * t)) * (0.7 + 0.3 * np.sin(2 * np.pi * 0.5 * t))
        fade = np.minimum(1, np.minimum(t / 1.0, (dur - t) / 0.8))
        return y * fade * 0.25
    if key == "end_sting":
        return (tone(523, 2.0, 0.7) + tone(659, 2.0, 0.7) + tone(784, 2.0, 0.7)) * 0.25
    if key.startswith("amb_"):
        n = int(dur * SR)
        y = np.cumsum(noise(n))
        y = y - lowpass(y, 2000)
        y /= np.max(np.abs(y)) + 1e-9
        return y * 0.5
    if key == "cat_chirp_shiro":
        return sweep(620, 900, 0.28, 20) * 0.4
    if key == "cat_low_shiro":
        return sweep(420, 380, 0.5, 8) * 0.3
    if key == "cat_low_mike":
        return sweep(300, 260, 0.7, 4) * 0.3
    if key == "cat_hiss_short":
        n = int(0.5 * SR)
        return np.diff(noise(n + 1)) * np.sin(np.pi * np.arange(n) / n) * 0.25
    if key == "cat_meow_panic_tora":
        return sweep(700, 1000, 0.3, 30) * 0.4
    if key == "cat_meow_calm_mike":
        return np.concatenate([sweep(480, 620, 0.3), sweep(620, 430, 0.35)]) * 0.3
    return None  # bgm_* など: 仮音は作らず無音


def find_asset(folder, key, exts):
    for e in exts:
        p = os.path.join(ROOT, folder, key + e)
        if os.path.exists(p):
            return p
    return None


def decode_audio(path):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64)


def build_mix(d, path):
    total = d["shots"][-1]["end"]
    mix = np.zeros(int(total * SR) + SR)
    used, missing = [], set()
    for shot in d["shots"]:
        for c in shot["sfx"]:
            dur = c.get("dur", 3.0)
            f = find_asset("audio", c["key"], (".wav", ".flac", ".mp3", ".ogg", ".m4a"))
            if f:
                y = decode_audio(f)
                if "dur" in c:
                    reps = int(math.ceil(dur * SR / max(len(y), 1)))
                    y = np.tile(y, reps)[: int(dur * SR)]
                used.append(f"{c['key']} <- {os.path.relpath(f, ROOT)}")
            else:
                y = synth(c["key"], dur)
                missing.add(c["key"])
                if y is None:
                    continue
            g = 10 ** (c.get("gain_db", 0) / 20)
            i = int(c["t"] * SR)
            j = min(len(mix), i + len(y))
            mix[i:j] += y[: j - i] * g
    mix = mix[: int(total * SR)]
    peak = np.max(np.abs(mix)) or 1.0
    mix = mix / peak * 0.89 if peak > 0.89 else mix
    pcm = (np.clip(mix, -1, 1) * 32767).astype("<i2")
    stereo = np.repeat(pcm[:, None], 2, axis=1)
    import wave
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(stereo.tobytes())
    return used, sorted(missing)


# -------------------------------------------------------------------- video

def placeholder_png(d, shot, path):
    from PIL import Image, ImageDraw, ImageFont
    w, h = d["resolution"]
    tint = [(38, 44, 56), (44, 52, 40), (56, 46, 36), (40, 36, 54), (58, 36, 36), (30, 40, 50)][shot["scene"] - 1]
    img = Image.new("RGB", (w, h), tint)
    dr = ImageDraw.Draw(img)
    big = ImageFont.truetype(FONT_FILE, 64)
    mid = ImageFont.truetype(FONT_FILE, 44)
    small = ImageFont.truetype(FONT_FILE, 34)
    dr.rectangle([120, 150, w - 120, 700], outline=(200, 200, 200), width=3)
    dr.text((160, 180), f"ANIMATIC 仮映像  {shot['id']}  [{shot['camera']}]", font=big, fill=(255, 210, 90))
    dr.text((160, 270), f"{shot['start']:.1f}–{shot['end']:.1f}s   登場: {' / '.join(shot['cats']) or '-'}", font=mid, fill=(230, 230, 230))
    y = 350
    for line in textwrap.wrap(shot["action_ja"], 36):
        dr.text((160, y), line, font=mid, fill=(255, 255, 255))
        y += 62
    dr.text((160, 640), f"未生成：clips/{shot['id']}.mp4 を置くと実映像に差し替わります", font=small, fill=(170, 170, 170))
    img.save(path)


def run(cmd):
    subprocess.run(cmd, check=True)


def render(d):
    fps = d["fps"]
    w, h = d["resolution"]
    tmp = os.path.join(ROOT, "build_tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    os.makedirs(os.path.join(ROOT, "output"), exist_ok=True)
    enc = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(fps), "-an"]
    segs, placeholders = [], []
    for shot in d["shots"]:
        dur = shot["end"] - shot["start"]
        frames = int(round(dur * fps))
        seg = os.path.join(tmp, f"seg_{shot['id']}.mp4")
        clip = find_asset("clips", shot["id"], (".mp4", ".mov", ".webm", ".mkv"))
        if clip:
            vf = (f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={fps},setsar=1,"
                  f"tpad=stop_mode=clone:stop_duration=10")
            run(["ffmpeg", "-v", "error", "-y", "-ss", str(shot.get("clip_in", 0)), "-i", clip,
                 "-vf", vf, "-frames:v", str(frames)] + enc + [seg])
        elif shot["camera"] == "CARD":
            run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c={shot.get('bg', '#000000')}:s={w}x{h}:r={fps}",
                 "-frames:v", str(frames)] + enc + [seg])
        else:
            png = os.path.join(tmp, f"ph_{shot['id']}.png")
            placeholder_png(d, shot, png)
            run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", png, "-vf", f"fps={fps},setsar=1",
                 "-frames:v", str(frames)] + enc + [seg])
            placeholders.append(shot["id"])
        segs.append(seg)

    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{s}'\n" for s in segs)
    video = os.path.join(tmp, "video.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video])

    mixwav = os.path.join(tmp, "mix.wav")
    used, missing = build_mix(d, mixwav)

    ass = os.path.join(ROOT, "subtitles", f"{d['project']}.ass")
    write_ass(d, ass)
    name = f"{d['project']}_final.mp4" if not placeholders else f"animatic_{d['project']}.mp4"
    out = os.path.join(ROOT, "output", name)
    fontsdir = os.path.dirname(FONT_FILE)
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", mixwav,
         "-vf", f"ass={ass}:fontsdir={fontsdir}",
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", str(SR), "-movflags", "+faststart", "-shortest", out])
    shutil.rmtree(tmp, ignore_errors=True)

    print(f"出力: {os.path.relpath(out, ROOT)}")
    if placeholders:
        print(f"仮映像のショット ({len(placeholders)}): {', '.join(placeholders)}")
    print(f"差し替え済み音源: {len(used)} 件")
    for u in used:
        print("  " + u)
    if missing:
        print(f"仮音/無音のままの音キー ({len(missing)}): {', '.join(missing)}")


def check(d):
    """タイミングと字幕の読みやすさを検査する。"""
    ok = True
    prev = 0.0
    for shot in d["shots"]:
        if abs(shot["start"] - prev) > 1e-6:
            print(f"[NG] {shot['id']} の開始 {shot['start']} が直前の終了 {prev} と不連続")
            ok = False
        prev = shot["end"]
        for s in shot["subs"]:
            n = len(s["text"].replace("\\N", ""))
            dur = s["end"] - s["start"]
            if s["start"] < shot["start"] - 1e-6 or s["end"] > shot["end"] + 1e-6:
                print(f"[NG] {shot['id']} 字幕がショット外: {s['text']}")
                ok = False
            if s["style"] in ("Shiro", "Tora", "Mike", "Narr") and n / dur > 9:
                print(f"[注意] {shot['id']} 読み速度 {n / dur:.1f}字/秒: {s['text']}")
    print(f"総尺: {prev:.1f} 秒 / ショット数: {len(d['shots'])}")
    return ok


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("docs", "render", "check"):
        print(__doc__)
        sys.exit(1)
    d = load()
    os.makedirs(os.path.join(ROOT, "subtitles"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "prompts"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    if not check(d):
        sys.exit(1)
    if sys.argv[1] in ("docs", "render"):
        write_srt(d, os.path.join(ROOT, "subtitles", f"{d['project']}.srt"))
        write_ass(d, os.path.join(ROOT, "subtitles", f"{d['project']}.ass"))
        write_prompts(d, os.path.join(ROOT, "prompts", "02_prompts.md"))
        write_script(d, os.path.join(ROOT, "docs", "01_script.md"))
        print("subtitles/ と prompts/ を更新しました")
    if sys.argv[1] == "render":
        render(d)


if __name__ == "__main__":
    main()
