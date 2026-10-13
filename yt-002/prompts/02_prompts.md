# YT-002 映像生成プロンプト（自動生成）

> このファイルは `tools/build.py docs` が `data/shots.json` から生成します。編集は shots.json 側で行ってください。

## 共通ネガティブプロンプト

```
human, person, human hands, human arms, fingers, human feet, clothing on cats, accessories, collar, standing on hind legs, bipedal, anthropomorphic, cartoon, anime, 3D render, CGI look, talking, mouth moving like speech, lip sync, human facial expression, smiling cat, eyebrows, extra legs, extra tails, missing legs, fused paws, deformed face, changing fur pattern, text, letters, subtitles, watermark, logo
```

## キャラクター記述ブロック（全プロンプトに一字一句同じ文を埋め込む）

- **SHIRO**: `Shiro: a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build`
- **TORA**: `Tora: a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings`
- **MIKE**: `Mike: an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture`

## ショット別

### S01（0.0–4.0s / 4.0秒 / DOORCAM）

- 内容: 玄関前のドアマットにミケが座り、インターホンのカメラをまっすぐ見上げる。ゆっくり首をかしげる。
- 参照画像: refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
footage from a doorbell security camera, fisheye wide-angle lens distortion, high angle looking down at the doormat, slight digital noise and compression artifacts, flat daylight, fixed static camera. Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) sits upright on a doormat in front of an apartment front door, looking straight up into the camera lens, then slowly tilts her head slightly. Outdoor corridor of a Japanese apartment building, concrete floor. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S02（4.0–7.0s / 3.0秒 / PHONE）

- 内容: ソファで丸くなっていたシロが顔を上げ、耳を玄関の方向へ回す。
- 参照画像: refs/shiro_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) is curled up on a light gray sofa, suddenly lifts her head, both ears rotate toward the left of frame (toward the front door), eyes wide and alert. Bright living room. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S03（7.0–9.5s / 2.5秒 / PHONE_CLOSE）

- 内容: ローテーブルの下で寝そべるトラ。瞳孔が開き、耳が後ろに倒れて固まる。
- 参照画像: refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 2.5 秒にトリム

```
handheld smartphone video at floor level, close-up, slight natural hand shake, natural window daylight, shallow depth of field. Close-up of Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) lying under a low wooden coffee table, his pupils dilate wide and his ears flatten backward, body freezes completely still. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S04（9.5–12.0s / 2.5秒 / DOORCAM）

- 内容: インターホン映像のミケにゆっくりデジタルズーム。ミケは瞬きせずカメラを見つめる。タイトル表示。
- 参照画像: refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 2.5 秒にトリム

```
footage from a doorbell security camera, fisheye wide-angle lens distortion, high angle looking down at the doormat, slight digital noise and compression artifacts, flat daylight, fixed static camera. Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) sits perfectly still on the doormat staring unblinking into the camera lens, slow digital zoom-in toward her face. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S05（12.0–16.0s / 4.0秒 / PHONE）

- 内容: 日の当たる窓辺に並んで座るシロとトラ。しっぽ同士が触れている。
- 参照画像: refs/shiro_*.png, refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) and Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) sit side by side on a sunny windowsill, both facing the window, their tails gently touching, relaxed. Warm afternoon light, lace curtain. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S06（16.0–20.0s / 4.0秒 / PHONE）

- 内容: トラがシロの頬に頭をこすりつける。シロはゆっくり瞬きする。
- 参照画像: refs/shiro_*.png, refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) affectionately rubs his head against the cheek of Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) (head bunting), she responds with a slow blink and leans in slightly. Same sunny windowsill. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S07（20.0–24.0s / 4.0秒 / PHONE）

- 内容: 並んだ2つの陶器の皿で、シロとトラが一緒にごはんを食べる。
- 参照画像: refs/shiro_*.png, refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) and Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) eat side by side from two small ceramic bowls on a kitchen floor mat, seen from a low three-quarter angle. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S08（24.0–27.0s / 3.0秒 / PHONE_CLOSE）

- 内容: トラが食べるのをやめ、耳が横を向き、目線がそれる。
- 参照画像: refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video at floor level, close-up, slight natural hand shake, natural window daylight, shallow depth of field. Close-up of Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) at a ceramic food bowl, he stops eating, his ears rotate sideways, and he looks away from the camera to the side, avoiding eye contact. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S09（27.0–30.0s / 3.0秒 / PHONE_CLOSE）

- 内容: ラグの上、トラの前足の横に置かれたスマホが光って振動する（画面の文字は編集で合成）。
- 参照画像: refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video at floor level, close-up, slight natural hand shake, natural window daylight, shallow depth of field. Floor-level close-up of a black smartphone lying face-up on a beige rug next to the orange striped front paw of Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings); the phone screen lights up with a plain bright glow and the phone vibrates on the rug. The cat's head turns quickly toward the phone. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S10（30.0–33.0s / 3.0秒 / PHONE_CLOSE）

- 内容: トラが前足をすばやく振り下ろし、スマホの画面を肉球でぴたっと押さえる。
- 参照画像: refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video at floor level, close-up, slight natural hand shake, natural window daylight, shallow depth of field. Floor-level close-up: Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) quickly brings one front paw down flat on top of the glowing smartphone, covering the screen with his paw pad, and holds it there. Realistic cat paw, four toes visible, no fingers. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S11（33.0–36.0s / 3.0秒 / PHONE）

- 内容: シロがゆっくり振り向き、目を細め、耳が少し横に開く。
- 参照画像: refs/shiro_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) slowly turns her head toward the camera-right, her eyes narrow into a suspicious squint and her ears rotate slightly outward. Living room background softly blurred. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S12（36.0–39.0s / 3.0秒 / PHONE_CLOSE）

- 内容: トラがスマホの上にそのまま香箱座りでのっかり、何事もない顔でゆっくり瞬き。
- 参照画像: refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video at floor level, close-up, slight natural hand shake, natural window daylight, shallow depth of field. Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) settles down and sits in a loaf position directly on top of the smartphone, hiding it completely under his body, then gives a slow innocent blink toward the camera. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S13（39.0–42.0s / 3.0秒 / PHONE_CLOSE）

- 内容: スマホの上で香箱座りのトラ。振動に合わせて体が小刻みに揺れる。手前にぼけたシロの白い後頭部。
- 参照画像: refs/tora_*.png, refs/shiro_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video at floor level, close-up, slight natural hand shake, natural window daylight, shallow depth of field. Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) sits in a loaf position on the floor, his body jiggles slightly in short rhythmic bursts as if something underneath him is vibrating; he keeps a stiff innocent face. In the blurred foreground, the white back of the head and ears of Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build), watching him. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S14（42.0–46.0s / 4.0秒 / DOORCAM）

- 内容: 冒頭と同じインターホン映像。ミケが座ってカメラを見上げる。
- 参照画像: refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
footage from a doorbell security camera, fisheye wide-angle lens distortion, high angle looking down at the doormat, slight digital noise and compression artifacts, flat daylight, fixed static camera. Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) sits upright on a doormat in front of an apartment front door, looking straight up into the camera lens. Outdoor corridor of a Japanese apartment building, concrete floor. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S15（46.0–50.0s / 4.0秒 / PHONE_CLOSE）

- 内容: 玄関ドアのペット用ドア（キャットフラップ）をミケが頭で押し開けて入ってくる。
- 参照画像: refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
handheld smartphone video at floor level, close-up, slight natural hand shake, natural window daylight, shallow depth of field. Low angle inside an apartment entryway: Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) pushes her head through a plastic pet flap in the bottom of the front door and steps inside, the flap swinging behind her. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S16（50.0–54.0s / 4.0秒 / SECCAM）

- 内容: 廊下の天井カメラ。ミケがしっぽを立てて、ゆっくりこちらへ歩いてくる。
- 参照画像: refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
footage from an indoor pet camera mounted high in a room corner, high-angle wide shot, slightly desaturated colors, mild compression artifacts, fixed static camera. Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) walks slowly and steadily down a narrow apartment hallway toward the camera, tail held upright, calm and deliberate steps, wooden floor. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S17（54.0–57.0s / 3.0秒 / PHONE）

- 内容: リビングの入口で立ち止まるミケ。正面を見据えたまま動かない。
- 参照画像: refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) stops at the threshold of a living room doorway, standing on four legs, staring straight ahead without moving, only the tip of her tail twitches. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S18（57.0–61.0s / 4.0秒 / SECCAM）

- 内容: リビング全景。入口にミケ、ソファにシロ、床の中央でトラが固まる三角配置。
- 参照画像: refs/mike_*.png, refs/shiro_*.png, refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
footage from an indoor pet camera mounted high in a room corner, high-angle wide shot, slightly desaturated colors, mild compression artifacts, fixed static camera. Wide high-angle view of a living room: Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) stands at the doorway on the left, Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) sits on a light gray sofa on the right, and Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) is frozen in the middle of the floor between them, looking back and forth. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S19（61.0–64.0s / 3.0秒 / PHONE）

- 内容: シロの耳が横に倒れ（イカ耳）、しっぽの毛がぶわっと膨らむ。
- 参照画像: refs/shiro_*.png
- 生成尺: 5秒で生成 → 編集で 3.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) on the sofa, her ears flatten sideways into airplane ears and her tail fur puffs up, body tense, eyes wide. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S20（64.0–68.0s / 4.0秒 / PHONE）

- 内容: トラが慌てて後ずさりし、フローリングで足が空回り。ティッシュ箱にぶつかって倒す。
- 参照画像: refs/tora_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) panics and scrambles backward on a slippery wooden floor, his paws slipping and skidding comically, then bumps into a tissue box which tips over. All four paws on the floor, natural cat movement. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S21（68.0–72.0s / 4.0秒 / PHONE）

- 内容: 床まであるカーテンの裏に隠れるトラ。しっぽと後ろ足だけが見えている。手前でシロとミケが並んでカーテンを見つめる。
- 参照画像: refs/tora_*.png, refs/shiro_*.png, refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. A floor-length beige curtain with a cat hiding behind it: only the ringed orange tail and orange hind paws of Tora (a large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings) stick out from under the curtain. In the foreground, seen from behind, Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) and Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) sit side by side staring at the curtain. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S22（72.0–77.0s / 5.0秒 / PHONE）

- 内容: 窓辺にひとりで座るシロへゆっくり寄る。逆光で、目線は下。
- 参照画像: refs/shiro_*.png
- 生成尺: 5秒で生成 → 編集で 5.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Slow push-in on Shiro (a slender adult female domestic shorthair cat, pure white short coat with no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build) sitting alone on a windowsill, backlit by soft afternoon light, gaze lowered to the floor, ears relaxed but slightly down, quiet melancholy mood. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S23（77.0–81.0s / 4.0秒 / PHONE）

- 内容: ミケが正面に座り、カメラをまっすぐ見つめる。静かな圧。
- 参照画像: refs/mike_*.png
- 生成尺: 5秒で生成 → 編集で 4.0 秒にトリム

```
handheld smartphone video, slight natural hand shake, natural window daylight, realistic home interior, shallow depth of field. Mike (an adult female calico domestic shorthair cat, white base coat with solid black and orange patches; black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back with an orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed posture) sits facing the camera directly, perfectly still, calm unblinking stare into the lens, slight slow push-in. photorealistic live-action footage of real domestic cats, natural feline anatomy and proportions, natural cat behavior, all cats stay on four legs, real fur texture, no text on screen.
```

### S24（81.0–87.0s / 6.0秒 / CARD）

- 内容: 暗い背景に問いのテロップ（生成不要）。
- 生成不要（編集でテキストカードを作成）

### S25（87.0–90.0s / 3.0秒 / CARD）

- 内容: エンドカード（生成不要）。
- 生成不要（編集でテキストカードを作成）
