# Loading GeoJSON 載入 GeoJSON

**Why 為什麼**: GeoJSON is the most common open-data vector format. Loading it correctly is the first step of every analysis.
GeoJSON 是最常見的開放資料向量格式，正確載入是每次分析的第一步。

## Steps 步驟

1. Open QGIS. 開啟 QGIS。
2. `Layer → Add Layer → Add Vector Layer…` 圖層 → 新增圖層 → 新增向量圖層…
3. Under **Source**, click `…` and select your `.geojson` file. 在「來源」處點擊 `…` 並選擇你的 `.geojson` 檔案。
4. Click **Add**. The layer appears in the Layers panel and on the canvas. 點擊「新增」，圖層將出現在圖層面板與畫布上。

> Tip 提示: You can also drag a `.geojson` file directly from your file explorer into the QGIS canvas.
> 你也可以直接將 `.geojson` 檔案從檔案總管拖曳至 QGIS 畫布。

![Screenshot placeholder: Add Vector Layer dialog with a GeoJSON file selected](placeholder-add-vector-layer.png)
*截圖佔位：新增向量圖層對話框，已選擇 GeoJSON 檔案*

## What to check right after loading 載入後應立即檢查

- Does the geometry appear in the expected location on the map? 幾何是否出現在地圖上預期的位置？
- Right-click layer → **Properties → Information** to see feature count and geometry type. 右鍵圖層 → 屬性 → 資訊，檢視要素數量與幾何類型。

Next: [Attribute Tables](attribute-tables.md) → [CRS](crs.md)
