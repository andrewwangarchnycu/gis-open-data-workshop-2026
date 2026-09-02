# Case Studies 案例研究

Real Taiwan open-data walkthroughs that extend the 2-hour core curriculum. The core workshop ([`lessons/`](../lessons/), [`notebooks/`](../notebooks/)) uses small hand-made sample data on purpose, so every learner gets identical, instant, network-independent results within the time budget. These case studies swap in **real datasets and real APIs** for learners who want to go further — as instructor live-demos, homework, or a starting point for an actual research project.

核心工作坊（[`lessons/`](../lessons/)、[`notebooks/`](../notebooks/)）刻意使用小型手造範例資料，讓每位學習者在時間限制內都能得到一致、即時、不依賴網路的結果。這些案例研究則換上**真實資料集與真實 API**，適合想進一步鑽研的學習者——可作為教師現場示範、課後作業，或實際研究專案的起點。

## Which one to use when 什麼時候用哪一個

| Case study 案例 | Data source 資料來源 | Registration 註冊門檻 | Recommended use 建議用途 |
|---|---|---|---|
| [01 — Green Coverage Grid](01-green-coverage-grid/) 綠覆率網格化 | data.taipei 臺北市行道樹及公園樹木分布圖 | None 無 | **Recommended default** for [Lesson 05](../lessons/05-computational-gis/) live demo and the [One Map Challenge](../exercises/04_one_map_challenge/) 建議作為[課程 05](../lessons/05-computational-gis/)現場示範與[一張地圖挑戰](../exercises/04_one_map_challenge/)的預設資料集 |
| [02 — Urban Heat Interpolation](02-urban-heat-interpolation/) 都市氣溫熱力圖 | Open-Meteo API (primary) / CWA opendata (advanced) | None for Open-Meteo; free key for CWA Open-Meteo 免申請；CWA 需免費金鑰 | Homework / extension after [Lesson 06](../lessons/06-spatial-insight/) — introduces spatial interpolation 課後延伸練習——介紹空間內插概念 |

## Why these are separate from `notebooks/` 為什麼與 `notebooks/` 分開放置

The core `notebooks/01`–`04` stay lightweight and dependency-free so the 2-hour session never stalls on a registration form, a rate limit, or a network hiccup. These `case-studies/` build directly on the same methods (buffer → join → calculate → visualize; interpolation) but point at datasets with real-world messiness: registration requirements, rate limits, coordinate systems that need checking, and API responses that need error handling.

核心的 `notebooks/01`–`04` 保持輕量、無外部依賴，讓 2 小時課程不會卡在註冊表單、呼叫額度或網路問題上。這些 `case-studies/` 沿用相同方法（緩衝區 → join → 計算 → 視覺化；內插），但改用具真實世界複雜度的資料集：需要註冊、有呼叫額度限制、座標系統需要確認、API 回應需要錯誤處理。

Each notebook below is written to **run end-to-end even without live credentials or network access** — it falls back to a clearly labeled offline/demo sample so you can learn the technique first and plug in real data second.
下方每份筆記本皆設計為**即使沒有真實憑證或網路連線也能完整執行**——會自動改用標示清楚的離線／示範範例，讓你先學會技巧，再接上真實資料。
