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

## Full worked examples 完整範例

See [`notebooks/`](../../notebooks/) for these patterns combined into complete pipelines.
完整流程範例請見 [`notebooks/`](../../notebooks/)。
