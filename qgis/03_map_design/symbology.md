# Basic Symbology 基本符號化

**Why 為什麼**: symbology is where the map starts answering your question visually. Color, size, and pattern should encode an attribute value — not just look nice.
符號化是地圖開始以視覺方式回答你問題之處。色彩、大小與圖案應該用來傳達屬性值，而不只是好看。

## Steps 步驟

1. Right-click layer → **Properties → Symbology**. 右鍵圖層 → 屬性 → 符號化。
2. Change the top dropdown from **Single Symbol** to one of: 將頂端下拉選單由「單一符號」改為以下之一：
   - **Graduated 分級符號** — for numeric attributes (e.g. tree density: light → dark) 用於數值屬性（例如樹木密度：淺到深）
   - **Categorized 分類符號** — for categorical attributes (e.g. land use type, one color per category) 用於類別屬性（例如土地利用類型，每類別一色）
3. Select the attribute **Value** to symbolize by. 選擇欲符號化的屬性欄位。
4. For Graduated: choose a **Color ramp** (prefer sequential ramps like `Greens` for ordered data) and number of classes. 分級符號：選擇色階（有序資料建議用連續型色階，如 `Greens`），並設定分級數量。
5. Click **Classify**, then **Apply**. 點擊「分類」，再點擊「套用」。

![Screenshot placeholder: Symbology panel set to Graduated, colored by tree_density](placeholder-symbology.png)
*截圖佔位：符號化面板設為分級符號，依 tree_density 上色*

## Matching color type to data type 依資料類型選用色彩類型

See full guide: [`resources/map-design/color-for-maps.md`](../../resources/map-design/color-for-maps.md)

| Data 資料 | Color type 色彩類型 |
|---|---|
| Ordered numeric (density, count) 有序數值（密度、數量） | Sequential 連續型 |
| Numeric with meaningful zero/midpoint (above/below average) 具意義中點的數值（高於／低於平均） | Diverging 發散型 |
| Unordered categories (land use type) 無序類別（土地利用類型） | Categorical 類別型 |

Next: [Layout Manager](layout-manager.md)
