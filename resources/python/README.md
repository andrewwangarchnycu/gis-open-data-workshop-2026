# Python Reference Python 參考資源

Cheat sheet for the small set of Python/GeoPandas patterns used across [`notebooks/`](../../notebooks/). Not a general Python course — just what this workshop needs.
本工作坊 [`notebooks/`](../../notebooks/) 中所使用的 Python／GeoPandas 常用語法速查表，並非通用 Python 課程，僅涵蓋本工作坊所需內容。

## Loading data 載入資料

```python
import geopandas as gpd

gdf = gpd.read_file("data.geojson")        # local or URL 本機或網址
gdf = gpd.read_file("https://.../data.geojson")
```

## Inspecting 檢視

```python
gdf.head()
gdf.shape
gdf.columns
gdf.crs
gdf.geom_type.unique()
gdf.geometry.isna().sum()
```

## Cleaning 清理

```python
gdf = gdf[gdf.geometry.notnull()]
gdf = gdf.dropna(subset=["some_column"])
gdf["col"] = gdf["col"].fillna("unknown")
```

## CRS / reprojection CRS／重新投影

```python
gdf.crs                          # check 檢查
gdf = gdf.set_crs("EPSG:4326")   # relabel only, no transform 僅重新標記，不轉換
gdf = gdf.to_crs("EPSG:3826")    # actually reproject/transform 實際重新投影／轉換
```

## Spatial operations 空間運算

```python
buffered = gdf.buffer(10)                              # buffer, in CRS units 緩衝區（以 CRS 單位計）
joined = gpd.sjoin(a, b, how="left", predicate="within")  # spatial join 空間 join
intersection = gpd.overlay(a, b, how="intersection")      # intersection 交集
```

## Calculating 計算

```python
gdf["area_m2"] = gdf.geometry.area      # requires a metric CRS 需公尺制 CRS
gdf.groupby("category").size()
```

## Visualizing 視覺化

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))
gdf.plot(ax=ax, column="value", cmap="Greens", legend=True)
plt.show()
```

## Chinese text in charts 圖表中顯示中文

Colab's default Matplotlib font (DejaVu Sans) can't render Chinese characters — they show up as boxes (□). All notebooks in this repo keep plot titles/legends in English for this reason. If you want Chinese text inside a chart itself, install a CJK font first:

Colab 預設的 Matplotlib 字型（DejaVu Sans）無法顯示中文，會變成方框（□）。本專案所有筆記本因此將圖表標題／圖例保持英文。若想在圖表內顯示中文，請先安裝支援中文的字型：

```python
# Run once per Colab session, before plotting 每個 Colab 工作階段執行一次，繪圖前執行
!apt-get -qq install fonts-noto-cjk > /dev/null
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK TC"]
plt.rcParams["axes.unicode_minus"] = False  # keep minus signs rendering correctly 確保負號正常顯示
```

## Point interpolation (IDW) 點狀資料內插

Used in [`case-studies/02-urban-heat-interpolation/`](../../case-studies/02-urban-heat-interpolation/) to turn scattered point measurements into a continuous surface — the computational equivalent of QGIS's Heatmap/IDW tool.

用於[`case-studies/02-urban-heat-interpolation/`](../../case-studies/02-urban-heat-interpolation/)，將離散點狀測量值轉換為連續空間場——相當於 QGIS Heatmap／IDW 工具的程式碼版本。

```python
from scipy.interpolate import griddata
import numpy as np

grid_x, grid_y = np.mgrid[lon_min:lon_max:200j, lat_min:lat_max:200j]
surface = griddata(points=np.column_stack([lons, lats]), values=measurements,
                    xi=(grid_x, grid_y), method="linear")
```

## Full worked examples 完整範例

See [`notebooks/`](../../notebooks/) for these patterns combined into complete pipelines.
完整流程範例請見 [`notebooks/`](../../notebooks/)。
