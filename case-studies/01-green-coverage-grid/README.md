# Case Study 01 — Green Coverage Grid, Taipei 綠覆率網格化：台北市

**Real dataset. No registration required.** 真實資料集，無需申請帳號。

## Research question 研究問題

Where in the city does tree coverage cluster, and where is it sparse? 城市中哪裡的樹木覆蓋較密集，哪裡較稀疏？

## Data 資料

| | |
|---|---|
| Dataset 資料集 | 臺北市行道樹及公園樹木分布圖 (Taipei street & park trees) |
| Publisher 提供機關 | 臺北市工務局公園處 |
| Portal 平台 | [data.taipei](https://data.taipei/dataset/detail?id=7a49d00c-a5ff-4a6b-be9e-aaa6dc1ff7e8) |
| Direct CSV 直接下載 | `https://tppkl.blob.core.windows.net/blobfs/TaipeiTree.csv` |
| License 授權 | Public / free 公開、免費 |
| CRS 座標系統 | TWD97 / TM2 zone 121 → **EPSG:3826** (already meters 已為公尺制) |

## Method 方法

```text
Load real schema (offline sample or live CSV)
↓
Build a 100m fishnet grid over the study area
↓
Spatial join: assign each tree to its grid cell
↓
Calculate: trees per hectare, per cell
↓
Visualize: choropleth grid map
```

This is the same buffer/join/calculate/visualize pipeline as [Lesson 05](../../lessons/05-computational-gis/) and [`notebooks/03_spatial_analysis.ipynb`](../../notebooks/03_spatial_analysis.ipynb) — the only difference is the dataset is real, and the grid (not administrative boundaries) is the unit of comparison.

## Run it 執行

[`notebook.ipynb`](notebook.ipynb) — [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/andrewwangarchnycu/gis-open-data-workshop-2026/blob/main/case-studies/01-green-coverage-grid/notebook.ipynb)

Runs instantly with a bundled offline sample (real schema and CRS, hand-placed points). Flip `FETCH_LIVE = True` inside the notebook (in Colab, which has full internet access) to pull the real, full-city dataset instead.

## Where this fits in the workshop 在工作坊中的定位

- Recommended as the live-demo dataset for [Lesson 05](../../lessons/05-computational-gis/) if the instructor wants a real-data example instead of (or alongside) the abstract sample. 若教師想在[課程 05](../../lessons/05-computational-gis/)中示範真實資料（取代或搭配抽象範例），建議使用本案例。
- Recommended default dataset for the [One Map Challenge](../../exercises/04_one_map_challenge/). 建議作為[一張地圖挑戰](../../exercises/04_one_map_challenge/)的預設資料集。
- Transfers directly to other cities: any point dataset (trees, benches, streetlights, CCTV, transit stops) + a study-area boundary reproduces this exact pipeline. 可直接套用至其他城市：任何點狀資料集（樹木、座椅、路燈、監視器、公車站）搭配研究範圍邊界，即可套用同一套流程。
