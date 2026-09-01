# Spatial Join 空間 Join

**Why 為什麼**: a spatial join attaches attributes from one layer to another *based on location*, not a shared ID column. This is how you answer questions like "how many trees fall inside each public space?"
空間 join 依據**位置**（而非共同的 ID 欄位）將一圖層的屬性附加至另一圖層。這是回答「每個公共空間內有幾棵樹？」這類問題的方法。

## Steps 步驟

1. `Vector → Data Management Tools → Join Attributes by Location…` 向量 → 資料管理工具 → 依位置 Join 屬性…
2. **Input layer**: the layer that receives new attributes (e.g. `public_spaces`). 輸入圖層：接收新屬性的圖層（例如 `public_spaces`）。
3. **Join layer**: the layer whose attributes/count you want to attach (e.g. `trees`). Join 圖層：欲附加屬性／計數的圖層（例如 `trees`）。
4. **Geometric predicate**: choose how they relate — `intersects`, `contains`, `within`, etc. 幾何判斷式：選擇關聯方式——相交、包含、位於內部等。
5. **Join type**: choose "one-to-many" and summarize (e.g. count) if multiple join-layer features match one input feature. Join 類型：若一個輸入要素對應多個 join 圖層要素，選擇「一對多」並彙總（例如計數）。
6. Click **Run**. 點擊「執行」。

![Screenshot placeholder: Join Attributes by Location dialog with predicate = contains](placeholder-spatial-join.png)
*截圖佔位：依位置 Join 屬性對話框，判斷式設為「包含」*

## Choosing the right predicate 選擇正確的判斷式

| Predicate 判斷式 | Meaning 意義 | Example use 範例用途 |
|---|---|---|
| `intersects` 相交 | Any overlap at all 任何重疊 | Buffer touches a public space 緩衝區碰觸公共空間 |
| `within` 位於內部 | Fully inside 完全在內部 | A tree point is inside a park polygon 樹木點位於公園面內 |
| `contains` 包含 | Fully contains the other 完全包含另一者 | A district contains a building 行政區包含建築 |

## Result 結果

The input layer's attribute table now has new columns from the join layer — e.g. a `tree_count` column on `public_spaces`. This is the QGIS equivalent of `gpd.sjoin()` in [Module 05](../../lessons/05-computational-gis/).
輸入圖層的屬性表現在會多出來自 join 圖層的新欄位——例如 `public_spaces` 多了 `tree_count` 欄位。這相當於[模組 05](../../lessons/05-computational-gis/)中的 `gpd.sjoin()`。

Next: [Intersection](intersection.md)
