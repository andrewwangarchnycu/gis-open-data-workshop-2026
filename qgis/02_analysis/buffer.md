# Buffer 緩衝區

**Why 為什麼**: a buffer turns a distance-based research question — "near," "within X meters," "adjacent to" — into an actual shape you can intersect or join against other data.
緩衝區將以距離為基礎的研究問題——「附近」、「X 公尺內」、「鄰接」——轉換為可與其他資料進行交集或 join 運算的實際形狀。

> Example 範例: *"We create a 10 m buffer because we want to ask which buildings are located within 10 m of vegetation."*
> 「我們建立 10 公尺緩衝區，是因為想知道哪些建築位於植栽 10 公尺範圍內。」

## Before you buffer 緩衝區運算前

Check your layer's CRS — buffer distance is measured in the CRS's units. Reproject to a metric CRS first if you want the distance in meters. See [CRS](../01_basics/crs.md).
先檢查圖層 CRS——緩衝距離以該 CRS 單位計算。若要以公尺為單位，需先重新投影至公尺制 CRS。

## Steps 步驟

1. `Vector → Geoprocessing Tools → Buffer…` 向量 → 地理處理工具 → 緩衝區…
2. **Input layer**: the layer to buffer around (e.g. `trees`). 輸入圖層：欲建立緩衝區的圖層（例如 `trees`）。
3. **Distance**: enter your value, e.g. `10` (in the layer's CRS units — meters if projected). 距離：輸入數值，例如 `10`（以圖層 CRS 單位計，若為投影 CRS 則為公尺）。
4. **Dissolve result**: check this if you want overlapping buffers merged into one shape. 若要將重疊緩衝區合併為單一形狀，勾選「融合結果」。
5. Click **Run**. A new buffer layer is created. 點擊「執行」，將產生新的緩衝區圖層。

![Screenshot placeholder: Buffer dialog with distance = 10 meters](placeholder-buffer-dialog.png)
*截圖佔位：緩衝區對話框，距離設為 10 公尺*

## Next step: use the buffer 下一步：運用緩衝區

A buffer alone rarely answers a question — combine it with:
單獨的緩衝區通常不足以回答問題，需搭配：

- [Spatial Join](spatial-join.md) — attach attributes based on what's inside the buffer 依緩衝區內容附加屬性
- [Intersection](intersection.md) — find the exact overlap between the buffer and another layer 找出緩衝區與另一圖層的精確重疊
