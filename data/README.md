# Data 資料

This folder is for **small, reproducible sample data** only. Notebooks embed their sample data directly in code (see [`notebooks/`](../notebooks/)) so they run standalone in Colab — files here are optional local copies for QGIS practice.
此資料夾僅存放**小型、可重現的範例資料**。筆記本已將範例資料直接內嵌於程式碼中（見 [`notebooks/`](../notebooks/)），使其能在 Colab 中獨立執行；此處檔案為供 QGIS 練習使用的選用本機副本。

## Structure 結構

- `raw/` — data as downloaded from a source, unmodified. 原始下載、未經修改的資料。
- `processed/` — cleaned/derived data produced by scripts in [`scripts/`](../scripts/). 由 [`scripts/`](../scripts/) 中的腳本清理／衍生出的資料。

## Rules 規則

1. **Do not commit large files.** Prefer files under a few MB; link to the original source for anything larger. 不要提交大型檔案，建議控制在數 MB 以內，較大檔案請連結至原始來源。
2. **Every file needs a source.** Note where it came from and its license in this README or a sidecar `.md`/`.txt` file. 每個檔案都須註明來源，於本 README 或附加的 `.md`／`.txt` 檔案中記錄來源與授權。
3. **Prefer GeoJSON/CSV** — readable, diffable, no proprietary format lock-in. 建議使用 GeoJSON／CSV——可讀、可比對差異、無專屬格式限制。

## Sample data used in this workshop 工作坊使用的範例資料

The trees / public-spaces sample used throughout `notebooks/` and `qgis/` is a small synthetic dataset inspired by a generic Taipei public-space context, defined directly in each notebook's code — see [`notebooks/01_open_data.ipynb`](../notebooks/01_open_data.ipynb).
貫穿 `notebooks/` 與 `qgis/` 使用的樹木／公共空間範例，是以一般化台北公共空間情境為靈感的小型合成資料集，直接定義於各筆記本程式碼中，見 [`notebooks/01_open_data.ipynb`](../notebooks/01_open_data.ipynb)。

For real data, start from [Lesson 03 — Finding Open Geospatial Data](../lessons/03-open-geospatial-data/).
如需真實資料，請從[課程 03 — 尋找開放地理資料](../lessons/03-open-geospatial-data/)開始。
