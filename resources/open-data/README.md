# Open Data Reference 開放資料參考資源

Curated starting points, organized by the categories in [Lesson 03](../../lessons/03-open-geospatial-data/). Always re-derive your dataset choice from your research question — see the logic chain there before browsing these.
依[課程 03](../../lessons/03-open-geospatial-data/)中的分類整理的入門資源。務必先從你的研究問題出發推導出所需資料，再瀏覽以下資源。

## General / global 綜合／全球

- [OpenStreetMap](https://www.openstreetmap.org) — buildings, roads, land use, POIs 建築、道路、土地利用、興趣點
- [Geofabrik](https://download.geofabrik.de) — bulk OSM downloads by region 依區域批次下載 OSM 資料
- [datacatalogs.org](https://datacatalogs.org) — index of open data portals worldwide 全球開放資料平台索引
- [HDX (Humanitarian Data Exchange)](https://data.humdata.org)

## Taiwan — general portals 台灣—綜合平台

- [data.gov.tw](https://data.gov.tw) — national open data portal 全國開放資料平台
- [data.taipei](https://data.taipei) — Taipei city open data portal 臺北市資料大平臺
- City-level portals (Taichung, Kaohsiung, Hsinchu, etc.) 各縣市開放資料平台

## Taiwan — datasets used in this repo's case studies 本專案案例研究所使用的具體資料集

Concrete, verified starting points — used directly in [`case-studies/`](../../case-studies/), not just abstract categories.
以下是本專案 [`case-studies/`](../../case-studies/) 實際使用的具體資料來源，而非泛泛的分類清單。

| Dataset 資料集 | Source 來源 | Registration 註冊 | Used in 使用於 |
|---|---|---|---|
| 臺北市行道樹及公園樹木分布圖 | [data.taipei](https://data.taipei/dataset/detail?id=7a49d00c-a5ff-4a6b-be9e-aaa6dc1ff7e8) | None 無 | [Case Study 01](../../case-studies/01-green-coverage-grid/) |
| Open-Meteo weather API | [open-meteo.com](https://open-meteo.com) | None 無 | [Case Study 02](../../case-studies/02-urban-heat-interpolation/) |
| 自動氣象站-氣象觀測資料 | [中央氣象署開放資料平臺](https://opendata.cwa.gov.tw) | Free account + API key 免費帳號＋API 金鑰 | [Case Study 02](../../case-studies/02-urban-heat-interpolation/) (advanced 進階) |

> ⚠️ **民生公共物聯網 (Civil IoT Taiwan)** was a useful source for environmental sensor data, but the government program formally concluded on 2025-12-31 and its old `sta.ci.taiwan.gov.tw` SensorThings API endpoint may no longer respond. Prefer CWA opendata or Open-Meteo for temperature/weather data instead (see [Case Study 02](../../case-studies/02-urban-heat-interpolation/)).
> **民生公共物聯網**過去是環境感測資料的實用來源，但該計畫已於 2025 年 12 月 31 日正式結束，舊有 `sta.ci.taiwan.gov.tw` SensorThings API 網址可能已不再回應。氣溫／氣象資料建議改用中央氣象署開放資料平台或 Open-Meteo（見[案例二](../../case-studies/02-urban-heat-interpolation/)）。

## Environmental 環境

- [Copernicus](https://www.copernicus.eu) — satellite/environmental data (EU) 衛星／環境資料
- [NASA Earthdata](https://earthdata.nasa.gov)
- [中央氣象署開放資料平臺](https://opendata.cwa.gov.tw) — free account required for API key 需免費註冊取得 API 金鑰

## Transport 運輸

- [TDX 運輸資料流通服務平臺](https://tdx.transportdata.tw) — buses, rail, bike-share, static + real-time; free registration, ~3 working days approval, HMAC auth 公車、軌道、公共自行車，含靜態與即時資料；免費註冊，審核約 3 個工作天，採 HMAC 認證
- OpenStreetMap road/bike network extracts OSM 道路／自行車道資料

## Weather 氣象

- [Open-Meteo API](https://open-meteo.com) — free, no-key weather API, supports batched multi-point queries 免費、免金鑰氣象 API，支援批次多點查詢
- [中央氣象署開放資料平臺](https://opendata.cwa.gov.tw) — authoritative physical station data, free API key required 權威實體測站資料，需免費申請 API 金鑰

## Evaluating any dataset 評估任何資料集

Before using a dataset, confirm 使用前請確認:

- [ ] Spatial coverage matches your study area 空間涵蓋範圍符合你的研究範圍
- [ ] Temporal coverage matches your question 時間涵蓋範圍符合你的問題
- [ ] License permits your intended use 授權條款允許你的預期用途
- [ ] Format and CRS are documented 格式與 CRS 有明確記載
