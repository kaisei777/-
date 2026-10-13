# YT-002『彼氏猫には、妻がいた。』90秒パイロット

## 現在の状態（正直な報告）

**完成動画（実写風の猫の映像）はまだ作れていません。** この作業環境には AI の映像生成ツールも画像生成ツールもないためです。

できているもの：

| 納品物 | 状態 | 場所 |
|---|---|---|
| 90秒の完成動画（MP4） | ❌ 未完成。代わりに **90秒のアニマティック（仮映像＋本番字幕＋仮の効果音）** を作成 | `output/animatic_YT-002.mp4` |
| シーン別台本 | ✅ | `docs/01_script.md` |
| 映像生成プロンプト | ✅ 全23ショット＋ネガティブプロンプト | `prompts/02_prompts.md` |
| キャラクター参照画像 | ⚠️ 仕様書と生成プロンプトのみ（画像は未生成） | `docs/03_character_refs.md` |
| 字幕データ（SRT） | ✅ 焼き込み用の ASS も作成 | `subtitles/` |
| 字幕・音響設計 | ✅ | `docs/04_sound_design.md` |
| 使用素材・ライセンス・費用・時間 | ✅ 実績（生成費 0 円）と本番の見積もり | `docs/05_license_cost_log.md` |
| 問題点・改善案・長尺化の手順 | ✅ | `docs/06_issues_and_scaling.md` |

## 仕組み

`data/shots.json` が唯一の正（ショットごとの尺、カメラ、登場する猫、プロンプト、字幕、効果音）です。ほかのファイルはすべてここから生成されます。

```bash
python3 tools/build.py check    # 尺の連続性と字幕の読む速さを検査
python3 tools/build.py docs     # 台本・プロンプト・SRT・ASS を再生成
python3 tools/build.py render   # 動画を組み立てる（ffmpeg、numpy、Pillow が必要）
```

## 完成させる手順

1. `docs/03_character_refs.md` に従って参照画像を作り、`refs/` に保存する
2. `prompts/02_prompts.md` のプロンプトで各ショットを生成し、`clips/S01.mp4` から `clips/S23.mp4` として保存する（尺の調整、拡大・トリミング、30fps への変換、音声の削除は自動）
3. 効果音・鳴き声を `audio/<キー>.wav` として置く（キーの一覧は `docs/04_sound_design.md`）
4. `python3 tools/build.py render` を実行する。仮映像が 1 つも残っていなければ `output/YT-002_final.mp4` が出力される（1 つでも残っていれば `animatic_` という名前になり、完成版と取り違えない）
5. 生成の記録を `docs/05_license_cost_log.md` のテンプレートに書き込む
6. YouTube へのアップロード時に、AI で生成したコンテンツであることを申告し、`subtitles/YT-002.srt` を字幕として登録する

## 出力の仕様
1920×1080、30fps、H.264（品質 CRF 18）、AAC 192kbps、音量 -14 LUFS、尺 90.0 秒。全編で「AI生成・創作再現」ラベルを表示し、冒頭と末尾にも注記を入れています。
