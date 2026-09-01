# Scripts 腳本

Optional local Python scripts that mirror the notebook workflow, for learners who want a reusable pipeline outside Colab (e.g. for their own capstone research).
選用的本機 Python 腳本，對應筆記本工作流程，供想在 Colab 之外建立可重複使用流程的學習者使用（例如用於個人期末研究）。

| Folder 資料夾 | Purpose 用途 | Mirrors 對應 |
|---|---|---|
| [`download/`](download/) | Pull data from open sources (OSM) 從開放來源（OSM）下載資料 | [Lesson 03](../lessons/03-open-geospatial-data/) |
| [`preprocessing/`](preprocessing/) | Clean and standardize raw data 清理並標準化原始資料 | [Lesson 05](../lessons/05-computational-gis/) Step: Load → Inspect → Clean |
| [`analysis/`](analysis/) | Run spatial analysis (buffer, join, density) 執行空間分析（緩衝區、join、密度） | [Lesson 05](../lessons/05-computational-gis/) Step: Spatial Operation → Calculate |

## Requirements 需求

```bash
pip install geopandas shapely osmnx
```

## Example pipeline 範例流程

```bash
python download/download_osm_data.py --place "Da'an District, Taipei, Taiwan" --tags leisure=park --out ../data/raw/parks.geojson
python preprocessing/clean_geodata.py --in ../data/raw/parks.geojson --out ../data/processed/parks_clean.geojson
python analysis/tree_density.py --trees ../data/processed/trees_clean.geojson --spaces ../data/processed/parks_clean.geojson --out ../data/processed/density.geojson
```

These scripts are optional — the notebooks in [`notebooks/`](../notebooks/) are self-contained and are the primary teaching path for this workshop.
這些腳本為選用項目——[`notebooks/`](../notebooks/) 中的筆記本已自成一體，為本工作坊的主要教學路徑。
