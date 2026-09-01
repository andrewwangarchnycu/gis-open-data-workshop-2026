# Filtering 篩選

**Why 為什麼**: filtering isolates the features relevant to your question, so every operation after it works on the right subset — not the entire dataset.
篩選能篩出與你問題相關的要素，讓後續每項操作都作用於正確的子集合，而非整個資料集。

## Steps 步驟

1. Right-click layer → **Filter…** (or **Properties → Source → Query Builder**). 右鍵圖層 → 篩選…（或屬性 → 來源 → 查詢建構器）。
2. Write an expression, e.g.: 寫入運算式，例如：

```sql
"height_m" > 20
```

```sql
"use" = 'public space'
```

```sql
"year_built" >= 2000 AND "height_m" < 15
```

3. Click **OK**. Only matching features remain visible/available. 點擊「確定」，僅符合條件的要素會顯示／可用。

![Screenshot placeholder: Query Builder with a height_m > 20 expression](placeholder-query-builder.png)
*截圖佔位：查詢建構器，內含 height_m > 20 運算式*

## Filter vs. Select 篩選 vs. 選取

| | Filter 篩選 | Select 選取 |
|---|---|---|
| Effect 效果 | Hides non-matching features from the layer entirely 將不符合的要素完全從圖層隱藏 | Highlights matching features but keeps all visible 反白符合要素但保留全部顯示 |
| Use for 適用於 | Narrowing a dataset before analysis 分析前縮小資料範圍 | Quick visual inspection 快速視覺檢查 |

## Connect it to your question 與問題連結

Before filtering, finish this sentence: *"I only need features where ___, because my question is about ___."*
篩選前，先完成這句話：「我只需要符合＿＿條件的要素，因為我的問題與＿＿有關。」

Next: [Buffer](../02_analysis/buffer.md)
