# Color for Maps 地圖用色

**Rule 規則**: color must encode information. Never choose a color scheme because it "looks nice" — choose it because it matches your data's structure.
色彩必須傳達資訊。絕不要因為「好看」而選擇配色，而要因為它符合你資料的結構。

## Three families 三種類型

### Sequential 連續型

For ordered numeric data, low to high. One hue, increasing in intensity.
用於有序數值資料，由低到高。單一色相，強度遞增。

> Example 範例: tree density (light green → dark green) 樹木密度（淺綠 → 深綠）

### Diverging 發散型

For numeric data with a meaningful midpoint (often zero, or an average). Two hues meeting at a neutral center.
用於具有意義中點（通常為零或平均值）的數值資料。兩個色相於中性中心點相接。

> Example 範例: temperature relative to citywide average (blue = below, white = average, red = above) 相對於全市平均的溫度（藍＝低於、白＝平均、紅＝高於）

### Categorical 類別型

For unordered categories. Distinct hues, no implied order.
用於無序類別。不同色相，不隱含順序。

> Example 範例: land use type (residential, commercial, industrial, green space — each a distinct color, no gradient) 土地利用類型（住宅、商業、工業、綠地——各自獨立顏色，無漸層關係）

## Choosing the wrong type — common mistakes 選錯類型——常見錯誤

- Using a rainbow/categorical palette for ordered numeric data — the eye can't read "order" from unrelated hues. 對有序數值資料使用彩虹／類別型配色——眼睛無法從不相關的色相中讀出「順序」。
- Using a sequential ramp for data with a meaningful zero — hides whether a value is above or below the reference point. 對具有意義零點的資料使用連續型色階——會掩蓋數值高於或低於參考點的資訊。

## Accessibility 無障礙設計

- Avoid red-green as your only distinguishing pair (common color-vision deficiency). 避免僅用紅綠作為唯一區分色（常見色覺辨識困難類型）。
- Check contrast — text and small symbols need to stay legible against your fill colors. 檢查對比度——文字與小型符號在色塊背景下仍需保持易讀。
- Prefer colorblind-safe palettes such as ColorBrewer (colorbrewer2.org). 建議使用色盲友善配色方案，如 ColorBrewer（colorbrewer2.org）。

## In QGIS / Matplotlib 於 QGIS／Matplotlib

- QGIS: `Properties → Symbology → Graduated`, choose a sequential/diverging color ramp. 選擇連續型／發散型色階。
- Matplotlib: `cmap="Greens"` (sequential), `cmap="RdBu"` (diverging), `cmap="tab10"` (categorical). `cmap="Greens"`（連續型）、`cmap="RdBu"`（發散型）、`cmap="tab10"`（類別型）。

Related: [Legend design](legend-design.md), [Figure-ground](figure-ground.md)
