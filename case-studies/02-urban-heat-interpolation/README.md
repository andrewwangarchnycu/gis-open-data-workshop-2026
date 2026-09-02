# Case Study 02 — Urban Heat Interpolation 都市氣溫熱力圖

**Real, live data. No registration required (primary source).** 真實即時資料，主要資料來源無需申請帳號。

## Research question 研究問題

At one moment in time, how does air temperature vary across the city, and where might heat pool? 在同一時刻，全市氣溫如何變化，哪裡可能是熱點？

## Data 資料

| | Primary 主要 | Advanced alternative 進階替代方案 |
|---|---|---|
| Source 來源 | [Open-Meteo API](https://open-meteo.com) | [中央氣象署開放資料平台](https://opendata.cwa.gov.tw) 自動氣象站觀測資料 |
| Registration 註冊 | None — free, no key 免申請、免金鑰 | Free account + personal API key 免費會員＋專屬 API 金鑰 |
| What it is 資料性質 | Modeled weather at any coordinate you choose ("virtual sensor network") 任意座標的模擬氣象資料（虛擬感測網） | Real physical station observations, fixed locations 真實測站觀測值，位置固定 |

> ⚠️ 民生公共物聯網 (Civil IoT Taiwan) is **not** used here: that government program concluded on 2025-12-31 and its old sensor API endpoint may no longer work. Use CWA opendata above for authoritative physical stations instead.
> 本案例**不**使用民生公共物聯網：該計畫已於 2025 年 12 月 31 日結束，舊有感測器 API 網址可能已失效。如需權威的實體測站資料，請改用上方的中央氣象署開放資料平台。

## Method 方法

```text
Choose a grid of coordinates (virtual sensor network)
↓
Query temperature at each point (Open-Meteo, one batched request)
↓
IDW / Kriging interpolation → continuous surface
↓
Visualize as a heatmap
```

This extends the buffer/interpolation reasoning from [Lesson 04](../../lessons/04-qgis-basics/) to a new operation: estimating values *between* known points, the computational equivalent of QGIS's Heatmap / IDW Interpolation tools.

## Run it 執行

[`notebook.ipynb`](notebook.ipynb) — [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/andrewwangarchnycu/gis-open-data-workshop-2026/blob/main/case-studies/02-urban-heat-interpolation/notebook.ipynb)

Tries a live Open-Meteo call first; falls back to a labeled synthetic temperature field if there's no network access, so it always runs end-to-end.

## Where this fits in the workshop 在工作坊中的定位

Positioned as a **post-workshop extension**, after [Lesson 06 — From Data to Spatial Insight](../../lessons/06-spatial-insight/): spatial interpolation is a genuinely new concept (not just a repeat of buffer/join), so it's better suited to self-paced follow-up than a live 20-minute segment.
定位為**課後延伸練習**，接續在[課程 06——從資料到空間洞見](../../lessons/06-spatial-insight/)之後：空間內插是真正的新概念（並非緩衝區／join 的重複），較適合自學延伸，而非塞進 20 分鐘的現場環節。
