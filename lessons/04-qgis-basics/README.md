# 04 — QGIS Basics QGIS 基礎
*20 minutes 分鐘*

QGIS is free, open-source desktop GIS software. In this module you learn only the operations you actually need — not the whole menu.
QGIS 是免費的開源桌面 GIS 軟體。本模組只教你真正需要的操作，而非整份選單。

> Every operation below follows: **Tool → Spatial Meaning → Research Question**
> 以下每個操作皆遵循：**工具 → 空間意義 → 研究問題**

Step-by-step guides with screenshots live in [`qgis/01_basics/`](../../qgis/01_basics/) and [`qgis/02_analysis/`](../../qgis/02_analysis/). This page gives the *reasoning*; those pages give the *clicks*.
含截圖的逐步教學位於 [`qgis/01_basics/`](../../qgis/01_basics/) 與 [`qgis/02_analysis/`](../../qgis/02_analysis/)。本頁說明**推理過程**，該頁面提供**實際操作步驟**。

## 1. Load data 載入資料

Drag a GeoJSON or CSV (with lat/lon columns) into QGIS. This is how your research question meets actual geometry for the first time.
將 GeoJSON 或含經緯度欄位的 CSV 拖入 QGIS。這是你的研究問題首次與實際幾何資料相遇的時刻。
→ Guide: [`qgis/01_basics/loading-geojson.md`](../../qgis/01_basics/loading-geojson.md), [`loading-csv.md`](../../qgis/01_basics/loading-csv.md)

## 2. Inspect attributes 檢視屬性

Open the attribute table. Ask: does this dataset actually contain the variable my question needs?
開啟屬性表。自問：這份資料集是否真的包含我問題所需的變數？
→ Guide: [`qgis/01_basics/attribute-tables.md`](../../qgis/01_basics/attribute-tables.md)

## 3. Check CRS 檢查 CRS

Confirm all layers share a CRS before doing anything else. Misaligned layers are the #1 beginner error.
在進行任何其他操作前，先確認所有圖層使用相同 CRS。圖層對不齊是初學者最常見的錯誤。
→ Guide: [`qgis/01_basics/crs.md`](../../qgis/01_basics/crs.md)

## 4. Filter 篩選

Isolate the features relevant to your question (e.g. buildings taller than 20m). This narrows the dataset to what actually matters.
篩選出與你問題相關的要素（例如高度超過 20 公尺的建築）。這能將資料集縮小至真正重要的部分。
→ Guide: [`qgis/01_basics/filtering.md`](../../qgis/01_basics/filtering.md)

## 5. Buffer 緩衝區

*Why we do this*: "We create a 10 m buffer because we want to ask which buildings are located within 10 m of vegetation."
**為什麼要做這件事**：「我們建立 10 公尺緩衝區，是因為想知道哪些建築位於植栽 10 公尺範圍內。」
A buffer turns a distance-based research question ("near," "within X meters") into a shape you can intersect with other data.
緩衝區將以距離為基礎的研究問題（「附近」、「X 公尺內」）轉換為可與其他資料進行交集運算的形狀。
→ Guide: [`qgis/02_analysis/buffer.md`](../../qgis/02_analysis/buffer.md)

## 6. Spatial Join 空間 Join

*Why*: attach attributes from one layer to another based on location — e.g. "how many trees fall inside each public space polygon?"
**為什麼**：依據位置將一圖層的屬性附加到另一圖層——例如「每個公共空間面內有幾棵樹？」
→ Guide: [`qgis/02_analysis/spatial-join.md`](../../qgis/02_analysis/spatial-join.md)

## 7. Intersection 交集

*Why*: find the exact overlapping geometry between two layers — e.g. "which part of this park overlaps the flood-risk zone?"
**為什麼**：找出兩圖層間精確重疊的幾何範圍——例如「這座公園哪個部分與洪水風險區重疊？」
→ Guide: [`qgis/02_analysis/intersection.md`](../../qgis/02_analysis/intersection.md)

## 8. Basic symbology 基本符號化

Color or size features by an attribute value so the map itself starts answering your question.
依屬性值為要素上色或調整大小，讓地圖本身開始回答你的問題。
→ Guide: [`qgis/03_map_design/symbology.md`](../../qgis/03_map_design/symbology.md)

## Focus: spatial reasoning over software commands 重點：空間推理優於軟體指令

Do not memorize menu paths. Memorize the *question each tool answers*:
不要死背選單路徑，要記住**每個工具回答的問題**：

| Tool 工具 | Question it answers 它回答的問題 |
|---|---|
| Filter 篩選 | Which features match a condition? 哪些要素符合條件？ |
| Buffer 緩衝區 | What's within X distance of this? 什麼東西在此範圍 X 公尺內？ |
| Spatial Join 空間 Join | What attributes does this location inherit from what it's inside/near? 此位置從其所在／鄰近範圍繼承了哪些屬性？ |
| Intersection 交集 | Where do two things overlap? 兩者在哪裡重疊？ |

Next: do these same operations in code, at scale, reproducibly — [Module 05](../05-computational-gis/).
接下來：以程式碼、規模化、可重現的方式執行相同操作——[模組 05](../05-computational-gis/)。
