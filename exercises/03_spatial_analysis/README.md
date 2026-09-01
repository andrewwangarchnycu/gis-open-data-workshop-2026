# Exercise 03 — Spatial Analysis in Colab Colab 空間分析練習

Pairs with [Lesson 05 — Computational GIS with Colab](../../lessons/05-computational-gis/) and [`notebooks/03_spatial_analysis.ipynb`](../../notebooks/03_spatial_analysis.ipynb).

## Task 任務

Open [`notebooks/04_mini_research.ipynb`](../../notebooks/04_mini_research.ipynb) in Colab and work through it using your own question from [Exercise 01](../01_data_exploration/), or the workshop sample data if you don't have your own dataset yet.
在 Colab 中開啟 [`notebooks/04_mini_research.ipynb`](../../notebooks/04_mini_research.ipynb)，套用[練習 01](../01_data_exploration/)中你自己的問題，若尚無自己的資料集則使用工作坊範例資料。

1. Load your data (or the sample). 載入你的資料（或範例資料）。
2. Inspect: shape, CRS, columns, missing values. 檢視：筆數、CRS、欄位、缺失值。
3. Clean: drop invalid geometry, fill/drop nulls. 清理：移除無效幾何、填補／刪除缺失值。
4. Reproject to a metric CRS. 重新投影至公尺制 CRS。
5. Run one spatial operation (buffer, join, or intersection) with a stated *why*. 執行一項空間運算（緩衝區、join 或交集），並說明「為什麼」。
6. Calculate one derived metric. 計算一項衍生指標。
7. Visualize with Matplotlib. 以 Matplotlib 視覺化。

## Deliverable 成果

A completed notebook cell output (screenshot or shared Colab link) showing your computed metric and a matplotlib figure, plus one sentence stating *why* you chose that spatial operation.
一份完成的筆記本輸出（截圖或 Colab 分享連結），呈現你計算出的指標與 matplotlib 圖表，並附上一句話說明你選擇該空間運算的原因。
