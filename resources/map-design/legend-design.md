# Legend Design 圖例設計

**Purpose 目的**: a legend decodes the symbols on your map. If a viewer needs to guess, the legend has failed.
圖例用來解讀地圖上的符號。若觀者需要猜測，代表圖例失敗了。

## Rules 規則

1. **Every color/symbol on the map must appear in the legend** — and vice versa. Don't leave unexplained colors on the map, or unused entries in the legend. 地圖上每個色彩／符號都須出現在圖例中，反之亦然。不要留下未說明的顏色，或圖例中未使用的項目。
2. **Order matters.** For sequential/diverging color ramps, list values low → high in the same visual order they appear on the ramp. 連續型／發散型色階應依數值由低到高排列，與色階視覺順序一致。
3. **Use real units**, not just relative labels. "0–2 trees / 1000m²" beats "Low." 使用實際單位，而非僅是相對標籤。「0–2 棵樹／千平方公尺」優於「低」。
4. **Keep it small and out of the way** — the legend supports the map, it should not compete with the main pattern for attention (see [visual hierarchy](visual-hierarchy.md)). 圖例應保持精簡並置於次要位置——它是輔助地圖，不應與主要樣式爭奪觀者注意力。

## Matching legend type to color type 圖例類型對應色彩類型

| Color type 色彩類型 | Legend style 圖例樣式 |
|---|---|
| Sequential 連續型 | A single continuous or stepped gradient bar with value labels 單一連續或分級的漸層色條，附數值標籤 |
| Diverging 發散型 | A gradient bar with the midpoint clearly marked (e.g. "0" or "average") 漸層色條，明確標示中點（例如「0」或「平均值」） |
| Categorical 類別型 | A list of color swatches, one per category, labeled by name 每類別一個色塊，標示類別名稱 |

## Common mistakes 常見錯誤

- Too many classes (more than ~5–7) — the eye can't distinguish that many shades. 分級過多（超過約 5–7 級）——眼睛無法辨識這麼多層次。
- Legend title missing units. 圖例標題缺少單位。
- Legend larger or more visually prominent than the map itself. 圖例比地圖本身更大或更顯眼。

Related: [Color for maps](color-for-maps.md), [Typography](typography.md)
