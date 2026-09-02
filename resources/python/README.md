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

## Map visualization: basemap & interactive maps 地圖視覺化：底圖與互動式地圖

A plot of colored shapes on white space doesn't read as a place. Two ways to fix that, used throughout [`notebooks/`](../../notebooks/) and [`case-studies/`](../../case-studies/):
在空白背景上畫幾個色塊，看起來不像一個真實地點。以下兩種方法可以解決這個問題，貫穿於 [`notebooks/`](../../notebooks/) 與 [`case-studies/`](../../case-studies/) 之中：

### Static basemap with `contextily` 靜態底圖（`contextily`）

Adds real street/building tiles underneath a normal `.plot()` — works with any CRS, since `contextily` reprojects the tiles to match your data.
在一般的 `.plot()` 圖層下方加入真實街道／建築底圖——可搭配任何 CRS，`contextily` 會自動將圖磚重新投影以對齊你的資料。

```python
import contextily as cx

fig, ax = plt.subplots(figsize=(7, 7))
gdf.plot(ax=ax, column="value", cmap="Greens", alpha=0.75, legend=True)
cx.add_basemap(ax, crs=gdf.crs.to_string(), source=cx.providers.CartoDB.Positron)
ax.set_axis_off()
plt.show()
```

> Keep `alpha < 1` on your data layer so the basemap underneath stays visible. 資料圖層的 `alpha` 建議小於 1，讓底下的底圖仍然可見。

### Interactive map with `folium` 互動式地圖（`folium`）

Best for *exploring* data — pan, zoom, click a feature for its attributes. Renders directly inline in a Colab cell (based on Leaflet.js), pre-installed in Colab.
最適合用於**探索**資料——可平移、縮放，點擊要素查看屬性。可直接於 Colab 儲存格中呈現（基於 Leaflet.js），Colab 已預先安裝。

```python
import folium

center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
m = folium.Map(location=center, zoom_start=15, tiles="OpenStreetMap")
folium.GeoJson(
    gdf,
    tooltip=folium.GeoJsonTooltip(fields=["name"]),
).add_to(m)
m  # displays inline in Colab / Jupyter 於 Colab／Jupyter 中直接顯示
```

For point data colored by a numeric value (e.g. temperature), use `folium.CircleMarker` per row with a `branca.colormap` scale instead of `GeoJson` — see [`case-studies/02-urban-heat-interpolation/`](../../case-studies/02-urban-heat-interpolation/).
若為依數值上色的點資料（例如溫度），可改用逐列的 `folium.CircleMarker` 搭配 `branca.colormap` 色階，而非 `GeoJson`——參見 [`case-studies/02-urban-heat-interpolation/`](../../case-studies/02-urban-heat-interpolation/)。

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
