# キャラクター参照画像 仕様書

**状態：未生成。** この作業環境には画像生成モデルがないため、参照画像は作れていません。以下は、画像生成ツールでそのまま使える仕様とプロンプトです。生成したら `refs/` フォルダに下記のファイル名で保存してください。

## 1. 共通ルール

| 項目 | 仕様 |
|---|---|
| 解像度 | 2048×2048（正方形）。全身カットは 2048×1536 も可 |
| 背景 | 単色のニュートラルグレー（#9A9A9A）。影は柔らかく、背景の模様は入れない |
| ライティング | 昼光色（5600K 前後）のソフトボックスを左前から。毛色が正しく見える露出 |
| カメラ | 50mm 相当。被写体は画面の 70% 程度の大きさ |
| 禁止 | 首輪・服・アクセサリー、人間の手、文字、透かし、擬人化した表情 |
| 左右の定義 | 「左」「右」は**猫自身から見た左右**。左右反転すると柄が崩れるため、編集で映像を反転しない |

## 2. 1匹あたりの必須カット（7枚）

| ファイル名 | 内容 | 主な用途 |
|---|---|---|
| `<name>_01_front.png` | 正面のお座り、顔はカメラ正対 | 顔・目の色の基準 |
| `<name>_02_3q_left.png` | 左斜め45°のお座り | 汎用（最もよく使う） |
| `<name>_03_3q_right.png` | 右斜め45°のお座り | 汎用 |
| `<name>_04_side.png` | 真横の立ち姿（四足） | 体格・しっぽ・背中の柄 |
| `<name>_05_back.png` | 後ろ姿のお座り | 後ろ姿のカット（S13、S21） |
| `<name>_06_loaf.png` | 香箱座り／寝そべり | 静止カット |
| `<name>_07_face_close.png` | 顔のアップ（目と鼻のディテール） | クローズアップの基準 |

正式版を決めたら、その7枚を**固定**します。以降の生成ではこの7枚から 2〜4 枚を参照画像として渡し、別のバリエーションを参照に混ぜないでください。

## 3. キャラクター定義

### シロ（`shiro`）
- **体格**：ほっそりした成猫のメス、約3.8kg。三匹の中でいちばん小さい
- **毛**：純白の短毛。**ぶち・まだらは一切なし**
- **目**：淡いミントグリーン（#B9E4C9 前後）。オッドアイや青い目にしない
- **鼻・耳の内側**：ピンク
- **見分けのポイント**：混じりけのない白と緑の目
- **演技**：耳の向き、細めた目、しっぽの膨らみで感情を表す

### トラ（`tora`）
- **体格**：がっしりした大柄の成猫のオス、約5.5kg。頬がふっくらしている
- **毛**：茶トラ（マッカレルタビー）の短毛。地はジンジャー、濃いオレンジの縞
- **白い部分**：あごと胸の小さなパッチのみ。**足先は白くしない**
- **額**：はっきりした「M」字
- **しっぽ**：オレンジに濃い色のリング
- **目**：琥珀色（#E0A030 前後）
- **見分けのポイント**：大きな体、M字、白いあご
- **演技**：耳が横を向く、目をそらす、ゆっくり瞬き、慌てて足が空回りする

### ミケ（`mike`）　※柄が複雑なため、固定するのが最も難しい
- **体格**：中くらいの成猫のメス、約4.2kg。背筋が伸び、落ち着いた姿勢
- **地色**：白
- **柄マップ（固定）**
  - 左耳と左目のまわり：黒
  - 右耳：オレンジ
  - 口元・胸・四本の足先：白
  - 背中：黒いサドル状の大きなパッチ
  - 左の腰：オレンジのパッチ
  - しっぽ：黒で、先端近くにオレンジの帯が1本
- **目**：黄緑（#C8D84A 前後）
- **見分けのポイント**：左右で非対称な顔（黒い左耳とオレンジの右耳）
- **演技**：ほとんど動かず、まっすぐ見つめる。しっぽの先だけが動く

> ミケの柄マップは、正式な正面・側面画像を作った後で、色分けした図（PNG）にして `refs/mike_pattern_map.png` として保存し、毎回の品質チェックで照合すること。

## 4. 参照画像生成プロンプト（英語。画像生成ツールにそのまま貼る）

共通の後半部分（`{VIEW}` を各カットに置き換える）：

```
, {VIEW}, studio reference photo for character consistency, neutral flat gray background (#9A9A9A), soft daylight key light from front-left, 50mm lens, sharp focus on fur texture, photorealistic, real domestic cat, natural feline anatomy, no collar, no accessories, no text, no humans
```

`{VIEW}` の置き換え例：`sitting upright facing the camera directly` / `sitting, three-quarter view turned to her left` / `standing on all four legs, full side profile facing right` / `sitting, seen from directly behind` / `lying in loaf position` / `close-up portrait of the face`

**シロ**
```
A slender adult female domestic shorthair cat with a pure white short coat and no markings at all, pale mint-green eyes, pink nose, pink inner ears, small neat head, medium-small build
```

**トラ**
```
A large stocky adult male orange mackerel tabby domestic shorthair cat, warm ginger coat with darker orange stripes, a clear 'M' marking on the forehead, white chin and a small white chest patch, orange paws (not white), amber eyes, round full cheeks, orange tail with darker rings
```

**ミケ**
```
An adult female calico domestic shorthair cat, white base coat with solid black and orange patches: black patch covering her left ear and surrounding her left eye, orange patch on her right ear, white muzzle, white chest and four white paws, black saddle patch on her back, orange patch on her left hip, black tail with one orange band near the tip, yellow-green eyes, medium build, composed upright posture
```

## 5. 作り方の手順

1. 画像モデルで正面カットを 20〜40 枚生成し、仕様に最も近い 1 枚を「マスター」に決める。
2. マスターを参照画像にして、残りの 6 カットを生成する。参照画像に対応した画像モデルや、画像編集モデル（Gemini の画像生成・編集、GPT の画像生成、FLUX Kontext、Midjourney の `--oref` など）を使う。
3. ミケは柄マップと 1 枚ずつ照合し、左右が逆になったものや、パッチが増えた・消えたものは不採用にする。
4. 3匹を並べた比較画像（`refs/lineup.png`）を作り、体格差（トラ ＞ ミケ ＞ シロ）が見て分かるか確認する。
5. 採用した画像のツール名・モデル・シード・プロンプト・日付を `docs/05_license_cost_log.md` に記録する。
