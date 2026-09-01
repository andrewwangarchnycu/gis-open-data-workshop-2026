# 07 — Research Map Design 研究地圖設計
*20 minutes 分鐘*

A research map communicates one insight clearly to someone who wasn't in the room. It should read as an **analytical diagram**, not a raw GIS export.
研究地圖是向未參與研究過程的人清楚傳達一項洞見。它應該讀起來像一張**分析圖表**，而不是 GIS 軟體的原始匯出畫面。

Full reference guides live in [`resources/map-design/`](../../resources/map-design/) — this page is the lecture summary.
完整參考指南位於 [`resources/map-design/`](../../resources/map-design/)——本頁為講授摘要。

## Visual hierarchy 視覺層級

**What should the viewer see first?** Decide this deliberately — usually the main spatial pattern, not the title or legend. Everything else should be visually subordinate.
**觀者應該先看到什麼？** 需刻意決定——通常是主要空間樣式，而非標題或圖例。其餘元素在視覺上應處於次要地位。
→ [`resources/map-design/visual-hierarchy.md`](../../resources/map-design/visual-hierarchy.md)

## Figure-ground 圖底關係

Borrowed directly from architectural drawing: what is figure (the subject of analysis) and what is ground (context)? A research map should make this distinction as deliberately as a Nolli map does.
直接借用自建築製圖：什麼是圖（分析主體）、什麼是底（脈絡背景）？研究地圖應如 Nolli 地圖般刻意做出這個區分。
→ [`resources/map-design/figure-ground.md`](../../resources/map-design/figure-ground.md)

## Color 色彩

Color must **encode information** — never decorate. Three families:
色彩必須**傳達資訊**——絕不是裝飾。三種類型：

- **Sequential 連續型** — ordered, low-to-high (e.g. tree density: light → dark green) 有序、由低到高（例如樹木密度：淺綠到深綠）
- **Diverging 發散型** — a meaningful midpoint (e.g. above/below average temperature) 具有意義的中點（例如高於／低於平均溫度）
- **Categorical 類別型** — unordered categories (e.g. land use type) 無序類別（例如土地利用類型）

→ [`resources/map-design/color-for-maps.md`](../../resources/map-design/color-for-maps.md)

## Typography 字體排印

Required text elements, in typical size order:
必要文字元素，依常見大小排序：

Title 標題 → Subtitle 副標題 → Legend 圖例 → Annotation 標註 → Data source 資料來源 → Scale 比例尺 → North arrow 指北針

→ [`resources/map-design/typography.md`](../../resources/map-design/typography.md)

## Annotation 標註

Point directly at the finding. A callout line and one sentence ("Historic core: lowest tree coverage") does more work than a paragraph in a caption.
直接指出發現所在。一條指引線加上一句話（「歷史核心區：樹木覆蓋率最低」）比圖說中的一整段文字更有效。
→ [`resources/map-design/annotation.md`](../../resources/map-design/annotation.md)

## Composition 構圖

- **Hierarchy 層級** — reinforce what matters most 強化最重要的內容
- **Whitespace 留白** — let the map breathe; don't fill every corner 讓地圖有呼吸空間，不要塞滿每個角落
- **Alignment 對齊** — elements align to a shared grid 元素對齊共同網格
- **Contrast 對比** — figure stands out clearly from ground 圖與底需有清楚對比
- **Legibility 易讀性** — text and symbols readable at final output size 文字與符號在最終輸出尺寸下需清晰可讀

## Recommended layout 建議版面

```text
┌──────────────────────────────────────────────┐
│ TITLE 標題                                    │
│ Research Question / Subtitle 研究問題／副標題 │
│                                                │
│              MAIN MAP 主要地圖                │
│              spatial pattern 空間樣式          │
│                                                │
│   ┌─────────┐                                 │
│   │ LEGEND  │       KEY INSIGHT 關鍵洞見       │
│   │ 圖例    │       Short explanation 簡短說明 │
│   └─────────┘                                 │
│                                                │
│ Data Source · Scale · North · Author           │
│ 資料來源 · 比例尺 · 指北針 · 作者              │
└──────────────────────────────────────────────┘
```

A4 landscape or 16:9. Inspired by architectural analytical diagrams, scientific visualization, and contemporary cartography — not decorative infographics.
建議使用 A4 橫向或 16:9 比例。靈感來自建築分析圖、科學視覺化與當代地圖學——而非裝飾性資訊圖表。

## Before you submit 提交前

Run your map through [`resources/map-design/research-map-checklist.md`](../../resources/map-design/research-map-checklist.md).
用 [`resources/map-design/research-map-checklist.md`](../../resources/map-design/research-map-checklist.md) 檢查你的地圖。

Next: [Module 08 — One Map Challenge](../../exercises/04_one_map_challenge/).
