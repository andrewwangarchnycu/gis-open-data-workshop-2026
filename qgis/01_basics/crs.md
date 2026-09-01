# Checking & Setting CRS 檢查與設定 CRS

**Why 為什麼**: layers with mismatched CRS will not align correctly, even if the data itself is perfectly correct. This is the single most common beginner error in GIS.
CRS 不一致的圖層即使資料本身完全正確，也無法正確對齊。這是 GIS 初學者最常見的錯誤。

See the concept explained in [Lesson 02 — From Space to Data](../../lessons/02-space-to-data/).

## Check a layer's CRS 檢查圖層 CRS

1. Right-click the layer → **Properties**. 右鍵圖層 → 屬性。
2. Go to the **Information** tab — the CRS is listed near the top. 前往「資訊」分頁，CRS 顯示於頂端附近。
3. Or check the bottom-right corner of the QGIS window — it shows the **project's** CRS. 或查看 QGIS 視窗右下角，顯示的是**專案**的 CRS。

![Screenshot placeholder: Layer Properties Information tab showing CRS](placeholder-crs-info.png)
*截圖佔位：圖層屬性資訊分頁顯示 CRS*

## Two different operations — don't confuse them 兩種不同操作——切勿混淆

| Operation 操作 | When to use 使用時機 |
|---|---|
| **Set CRS** (`Layer → Set CRS`) 設定 CRS | The layer's CRS is *labeled wrong* but the coordinates themselves are fine — you're just correcting the label. 圖層 CRS 標籤錯誤，但座標本身正確——只是修正標籤。 |
| **Reproject / Export with CRS** (`Layer → Save As…`, choose a new CRS) 重新投影／以新 CRS 匯出 | The coordinates need to actually be *transformed* into a different CRS (e.g. for accurate distance/area in meters). 座標需要實際**轉換**至另一 CRS（例如需要精確的公尺制距離／面積）。 |

## Which CRS to use 該用哪種 CRS

- **EPSG:4326 (WGS 84)** — standard lon/lat, good for storing/sharing data, but distances/areas are in degrees (not useful for buffers). 標準經緯度，適合儲存／分享資料，但距離／面積單位為度（不適合緩衝區運算）。
- **A local projected CRS** (e.g. EPSG:3826 for Taiwan) — use this before measuring distance, area, or creating a buffer in meters. 進行距離、面積測量或以公尺為單位建立緩衝區前，應使用此類 CRS。

> **Rule of thumb 經驗法則**: store and share in EPSG:4326; reproject to a local metric CRS right before any measurement operation.
> 儲存與分享用 EPSG:4326；在進行任何測量運算前，重新投影至當地公尺制 CRS。

Next: [Filtering](filtering.md) → [Buffer](../02_analysis/buffer.md)
