# 02 — From Space to Data 從空間到資料
*15 minutes 分鐘*

Spatial reality is continuous; data is not. This module teaches how architectural space gets encoded as data — and what's lost or gained in the process.
真實空間是連續的，資料卻不是。本模組說明建築空間如何被編碼為資料，以及這個過程中失去或獲得了什麼。

## Vector vs. Raster 向量與網格

| | Vector 向量 | Raster 網格 |
|---|---|---|
| Structure 結構 | Discrete geometries (points, lines, polygons) 離散幾何（點、線、面） | Grid of cells/pixels, each with a value 由格網／像元組成，每格皆有一個數值 |
| Architectural example 建築範例 | A building footprint drawn as a polygon 以多邊形繪製的建築足跡 | A satellite image, a DEM (elevation raster) 衛星影像、DEM（高程網格） |
| Good for 適合用於 | Discrete objects: buildings, roads, parcels 離散物件：建築、道路、地籍 | Continuous phenomena: temperature, elevation, land cover 連續現象：溫度、高程、地表覆蓋 |

## Point, Line, Polygon 點、線、面

Vector data has three basic geometry types — and architecture already thinks in exactly these terms:
向量資料有三種基本幾何類型——而建築思考方式本就是如此：

- **Point 點** — a tree, a lamppost, a building entrance 一棵樹、一根路燈、一個建築入口
- **Line 線** — a street centerline, a walking path, a river 街道中心線、步行路徑、河流
- **Polygon 面** — a building footprint, a park boundary, a land parcel 建築足跡、公園邊界、地籍範圍

## Attributes 屬性資料

Every geometry carries a table of attributes — the "non-spatial" facts attached to a spatial object.
每個幾何物件都附帶一張屬性表——附加於空間物件上的「非空間」事實資料。

Example: a building footprint (polygon) might carry:
範例：一個建築足跡（面）可能帶有以下屬性：

| id | height_m | year_built | use |
|---|---|---|---|
| 001 | 24.5 | 1998 | residential |
| 002 | 12.0 | 2015 | mixed-use |

The geometry answers "where." The attributes answer "what."
幾何回答「在哪裡」，屬性回答「是什麼」。

## Coordinates 座標

A coordinate is a numeric address for a location — typically (longitude, latitude) for geographic coordinates, or (x, y) for projected coordinates. The key idea: a coordinate is meaningless without knowing *which reference system* it's measured in.
座標是位置的數值地址——地理座標通常為（經度、緯度），投影座標則為（x, y）。關鍵概念：若不知道座標是依據**哪個參考系統**測量，該座標便毫無意義。

## CRS — Coordinate Reference System 座標參考系統

A CRS defines how coordinates relate to actual locations on Earth — the "shared language" that lets different datasets line up.
CRS 定義了座標如何對應到地球上的實際位置——是讓不同資料集能夠對齊的「共通語言」。

Architectural analogy: two site plans drawn at different scales or from different origin points won't overlay correctly until you align them to a shared reference. CRS is that shared reference, for the whole planet.
建築類比：兩張以不同比例尺或不同原點繪製的基地圖，若未對齊到共同參考點就無法正確疊合。CRS 就是全球尺度上的那個共同參考點。

> **Common failure mode**: two layers look "in the wrong place" when overlaid. 90% of the time, it's a CRS mismatch, not bad data.
> **常見錯誤**：兩個圖層疊合後「位置對不上」，九成情況並非資料有誤，而是 CRS 不一致。

We'll check and fix CRS hands-on in [Module 04 — QGIS Basics](../04-qgis-basics/) and [Module 05 — Computational GIS](../05-computational-gis/).
我們會在[模組 04 — QGIS 基礎](../04-qgis-basics/)與[模組 05 — 運算式 GIS](../05-computational-gis/)中實際檢查與修正 CRS。

## Quick check 快速檢查

For each item, is it vector or raster, and if vector, point/line/polygon?
以下每項是向量還是網格？若為向量，屬於點、線還是面？

1. A bus stop 公車站牌
2. A land-surface-temperature satellite image 地表溫度衛星影像
3. A bike lane 自行車道
4. A public plaza boundary 公共廣場邊界
