# Attribute Tables 屬性表

**Why 為什麼**: geometry tells you *where*; the attribute table tells you *what*. Before analyzing anything, confirm the table actually contains the variable your research question needs.
幾何告訴你「在哪裡」；屬性表告訴你「是什麼」。在分析前，先確認屬性表確實包含你研究問題所需的變數。

## Open the attribute table 開啟屬性表

1. Right-click a layer → **Open Attribute Table** (or select the layer and press `F6`). 右鍵圖層 → 開啟屬性表（或選取圖層後按 `F6`）。
2. Each row = one feature (a point, line, or polygon). Each column = one attribute. 每列代表一個要素（點、線或面），每欄代表一個屬性。

![Screenshot placeholder: Attribute table with columns like height_m, year_built, use](placeholder-attribute-table.png)
*截圖佔位：屬性表，含 height_m、year_built、use 等欄位*

## Useful things to do here 常用操作

- **Select by clicking a row** — the matching feature highlights on the map (and vice versa). 點選某列——地圖上對應要素會被反白（反之亦然）。
- **Sort by a column** — click the column header. 依欄位排序——點擊欄位標題。
- **Field calculator** (`Ctrl+I`) — create a new attribute computed from existing ones (e.g. area in m²). 欄位計算機——由既有欄位計算出新屬性（例如平方公尺面積）。

## Reading a table with a research question in mind 帶著研究問題閱讀表格

Ask 自問:

- Which column holds the variable I need? 哪個欄位是我需要的變數？
- Are there missing/null values? 是否有缺失值？
- Are categorical values consistent (e.g. `"Park"` vs `"park"` vs `"PARK"`)? 類別值是否一致（例如 `"Park"` 對比 `"park"`）？

Next: [Filtering](filtering.md)
