# 05 — Computational GIS with Google Colab 用 Google Colab 做運算式 GIS
*20 minutes 分鐘*

QGIS lets you *see* spatial operations happen one click at a time. Code lets you *compute* the same operations reproducibly, at scale, and share the exact steps with anyone.
QGIS 讓你一步步「看見」空間操作發生的過程。程式碼則讓你以可重現、可規模化的方式「運算」相同操作，並能與任何人分享確切步驟。

All coding in this workshop happens in **Google Colab** — nothing to install locally.
本工作坊所有程式操作皆在 **Google Colab** 中進行——不需在本機安裝任何軟體。

## Tools 工具

| Library 套件 | Role 角色 |
|---|---|
| `pandas` | Tabular data 表格資料 |
| `geopandas` | Spatial data — pandas + geometry 空間資料——pandas 加上幾何 |
| `shapely` | Geometry objects and operations 幾何物件與運算 |
| `matplotlib` | Visualization 視覺化 |
| `osmnx` (when needed 需要時) | Download OpenStreetMap data directly 直接下載 OpenStreetMap 資料 |

## The workflow 工作流程

```text
Load 載入
↓
Inspect 檢視
↓
Clean 清理
↓
Spatial Operation 空間運算
↓
Calculate 計算
↓
Visualize 視覺化
```

This mirrors the QGIS workflow from [Module 04](../04-qgis-basics/) exactly — same reasoning, different tool.
這與[模組 04](../04-qgis-basics/)的 QGIS 工作流程完全對應——推理相同，工具不同。

## Minimal example 最小範例

```python
# Install (Colab already has most of these, but this is explicit and reproducible)
!pip install geopandas shapely matplotlib -q

import geopandas as gpd
import matplotlib.pyplot as plt

# Load — a small GeoJSON of public spaces
public_spaces = gpd.read_file("public_spaces.geojson")

# Inspect
print(public_spaces.head())
print(public_spaces.crs)

# Clean — drop rows with missing geometry
public_spaces = public_spaces[public_spaces.geometry.notnull()]

# Spatial Operation — buffer trees by 10m, same reasoning as QGIS Module 04 step 5
trees = gpd.read_file("trees.geojson").to_crs(public_spaces.crs)
tree_buffers = trees.buffer(10)

# Calculate — how many public spaces contain at least one tree buffer?
public_spaces["has_nearby_tree"] = public_spaces.geometry.apply(
    lambda space: tree_buffers.intersects(space).any()
)

# Visualize
fig, ax = plt.subplots(figsize=(8, 8))
public_spaces.plot(ax=ax, column="has_nearby_tree", legend=True, cmap="Greens")
plt.title("Public spaces with nearby trees")
plt.show()
```

Every step maps back to a QGIS operation you already understand — `buffer()` is the Buffer tool, `.intersects()` is Spatial Join/Intersection logic, `.plot()` is Symbology.
每個步驟都對應到你已理解的 QGIS 操作——`buffer()` 對應緩衝區工具，`.intersects()` 對應空間 Join／交集邏輯，`.plot()` 對應符號化。

## Hands-on notebooks 實作筆記本

Work through these in order — each builds on the last:
依序完成以下筆記本，每份皆建立在前一份的基礎上：

1. [`notebooks/01_open_data.ipynb`](../../notebooks/01_open_data.ipynb) — find & load open data 尋找並載入開放資料
2. [`notebooks/02_geodata_exploration.ipynb`](../../notebooks/02_geodata_exploration.ipynb) — inspect & clean 檢視與清理
3. [`notebooks/03_spatial_analysis.ipynb`](../../notebooks/03_spatial_analysis.ipynb) — buffer, join, calculate 緩衝區、join、計算
4. [`notebooks/04_mini_research.ipynb`](../../notebooks/04_mini_research.ipynb) — full pipeline on your own question 以你自己的問題執行完整流程

## Keep it beginner-friendly 保持初學者友善

- Every notebook installs its own dependencies in the first cell. 每份筆記本的第一個儲存格皆自動安裝所需套件。
- Datasets are small and load in seconds. 資料集小巧，可在數秒內載入。
- Comments explain spatial meaning, not just syntax. 註解說明空間意義，而非僅是語法。

Next: turn the computed result into an interpretation — [Module 06](../06-spatial-insight/).
接下來：把運算結果轉譯為詮釋——[模組 06](../06-spatial-insight/)。
