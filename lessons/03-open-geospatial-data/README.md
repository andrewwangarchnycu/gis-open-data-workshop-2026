# 03 — Finding Open Geospatial Data 尋找開放地理資料
*15 minutes 分鐘*

## The logic 邏輯順序

Never browse an open data portal looking for "something interesting." Work backwards from your question.
不要漫無目的瀏覽開放資料平台找「有趣的東西」，而是從你的問題反推。

```text
Research Question 研究問題
↓
Required Variables 所需變數
↓
Potential Dataset 可能的資料集
↓
Data Source 資料來源
↓
Spatial Dataset 空間資料集
```

**Example 範例:**

- Question 問題: "Where are the greener public spaces?" 「哪裡是較綠意盎然的公共空間？」
- Required variables 所需變數: tree locations, public space boundaries 樹木位置、公共空間邊界
- Potential dataset 可能資料集: street tree inventory, park/plaza polygons 行道樹清冊、公園／廣場面資料
- Data source 資料來源: city open data portal, OpenStreetMap 城市開放資料平台、OpenStreetMap
- Spatial dataset 空間資料集: `trees.geojson`, `public_spaces.geojson`

## Where to look 去哪裡找

### OpenStreetMap (OSM)

A free, editable, global map database. Buildings, roads, land use, points of interest — all downloadable as vector data.
免費、可編輯的全球地圖資料庫。建築、道路、土地利用、興趣點——皆可下載為向量資料。

- Browser: [openstreetmap.org](https://www.openstreetmap.org)
- Bulk download: [Geofabrik](https://download.geofabrik.de)
- Python access: `osmnx` (see [Module 05](../05-computational-gis/))

### Government open data 政府開放資料

Most national/city governments publish open portals with zoning, land use, transit, environmental sensors, cadastral (land parcel) data.
多數國家／城市政府設有開放資料平台，提供分區、土地利用、大眾運輸、環境感測、地籍資料。

- Taiwan: [data.gov.tw](https://data.gov.tw)
- Global index: [datacatalogs.org](https://datacatalogs.org)

### APIs

Live or on-demand data accessed via code instead of a manual download — useful for weather, transit, or frequently updated data.
透過程式碼即時或依需求存取的資料，而非手動下載——適合天氣、運輸或頻繁更新的資料。

### Environmental data 環境資料

Air quality, temperature, land cover, elevation (DEM). Sources: national meteorological agencies, Copernicus, NASA Earthdata.
空氣品質、氣溫、地表覆蓋、高程（DEM）。來源：國家氣象機構、Copernicus、NASA Earthdata。

### Transport data 運輸資料

Bus/metro routes and stops, bike-share stations, road networks. Often published as GTFS (transit) or via OSM.
公車／捷運路線與站點、共享單車站點、道路網絡。常以 GTFS（大眾運輸格式）發布，或包含於 OSM 中。

### Weather data 氣象資料

Temperature, humidity, wind — useful for environmental/comfort-related research. Sources: national weather services, Open-Meteo API.
氣溫、濕度、風——適用於環境／舒適度相關研究。來源：國家氣象單位、Open-Meteo API。

## Evaluating a dataset before you use it 使用前評估資料集

Ask before downloading 下載前先問自己：

- [ ] Does it cover my study area? 是否涵蓋我的研究範圍？
- [ ] Does it cover the right time period? 是否涵蓋正確的時間範圍？
- [ ] What's the license — can I use and share it? 授權條款為何——是否可使用與分享？
- [ ] What format is it in (GeoJSON, Shapefile, CSV with coordinates)? 格式為何（GeoJSON、Shapefile、含座標的 CSV）？
- [ ] What CRS is it in? 使用哪種 CRS？

## Try it 動手試

Take the question you wrote in [Module 01](../01-mapping-the-unknown/) and fill in this chain:
拿出你在[模組 01](../01-mapping-the-unknown/)寫下的問題，填入以下鏈：

```text
My question 我的問題: ___________________________
Required variables 所需變數: ___________________________
Potential dataset 可能資料集: ___________________________
Data source 資料來源: ___________________________
```

We'll use exactly this pattern hands-on in [`notebooks/01_open_data.ipynb`](../../notebooks/01_open_data.ipynb).
我們會在 [`notebooks/01_open_data.ipynb`](../../notebooks/01_open_data.ipynb) 中實際運用這個模式。
