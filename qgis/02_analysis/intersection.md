# Intersection 交集

**Why 為什麼**: intersection computes the exact overlapping geometry between two layers — not just "do they touch," but the precise shared shape. Use it when the *area* or *shape* of overlap itself matters.
交集運算計算兩圖層間精確重疊的幾何形狀，不只是「是否碰觸」，而是精確的共享形狀。當重疊的**面積**或**形狀**本身具有意義時使用此工具。

> Example 範例: *"Which part of this park overlaps the flood-risk zone?"*
> 「這座公園哪個部分與洪水風險區重疊？」

## Steps 步驟

1. `Vector → Geoprocessing Tools → Intersection…` 向量 → 地理處理工具 → 交集…
2. **Input layer**: first layer (e.g. `parks`). 輸入圖層：第一個圖層（例如 `parks`）。
3. **Overlay layer**: second layer (e.g. `flood_risk_zones`). 疊加圖層：第二個圖層（例如 `flood_risk_zones`）。
4. Click **Run**. The output contains only the overlapping geometry, with attributes from both layers. 點擊「執行」，輸出僅包含重疊幾何，並帶有兩圖層的屬性。

![Screenshot placeholder: Intersection dialog with two input layers selected](placeholder-intersection.png)
*截圖佔位：交集對話框，已選擇兩個輸入圖層*

## Intersection vs. Spatial Join 交集 vs. 空間 Join

| | Intersection 交集 | Spatial Join 空間 Join |
|---|---|---|
| Output geometry 輸出幾何 | New, clipped to the overlap 新產生，裁切至重疊範圍 | Unchanged from input layer 與輸入圖層相同，不變 |
| Use when 使用時機 | You need the overlapping *shape/area* itself 需要重疊的**形狀／面積**本身 | You need to *attach attributes* based on location 需要依位置**附加屬性** |

## Follow-up 後續步驟

After intersecting, use the Field Calculator to compute the overlap area (`$area`) — this is often the metric that answers the research question directly.
交集運算後，可用欄位計算機計算重疊面積（`$area`）——這往往是直接回答研究問題的指標。

Next: [Symbology](../03_map_design/symbology.md)
