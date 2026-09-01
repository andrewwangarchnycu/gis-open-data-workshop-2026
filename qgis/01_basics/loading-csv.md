# Loading CSV (with coordinates) 載入 CSV（含座標）

**Why 為什麼**: many open datasets (weather stations, survey points, sensor readings) come as plain CSV with latitude/longitude columns, not as ready-made spatial files. QGIS can turn these into a spatial layer.
許多開放資料（氣象站、調查點、感測器數值）以純 CSV 形式提供，僅含經緯度欄位，而非現成的空間檔案。QGIS 可將其轉換為空間圖層。

## Requirements 前提條件

Your CSV needs two numeric columns for coordinates, e.g. `lon`, `lat` (or `x`, `y`).
你的 CSV 需含兩個數值座標欄位，例如 `lon`、`lat`（或 `x`、`y`）。

## Steps 步驟

1. `Layer → Add Layer → Add Delimited Text Layer…` 圖層 → 新增圖層 → 新增分隔文字圖層…
2. Select your `.csv` file. QGIS auto-detects the delimiter (comma). 選擇你的 `.csv` 檔案，QGIS 會自動偵測分隔符號（逗號）。
3. Under **Geometry Definition**, choose **Point coordinates** and set the X field (longitude) and Y field (latitude). 於「幾何定義」選擇「點座標」，設定 X 欄位（經度）與 Y 欄位（緯度）。
4. Set the **Geometry CRS** — usually `EPSG:4326 - WGS 84` for raw lon/lat data. 設定「幾何 CRS」——經緯度原始資料通常為 `EPSG:4326 - WGS 84`。
5. Click **Add**. 點擊「新增」。

![Screenshot placeholder: Add Delimited Text Layer dialog with X/Y fields set](placeholder-delimited-text.png)
*截圖佔位：新增分隔文字圖層對話框，已設定 X／Y 欄位*

> **Common mistake 常見錯誤**: swapping X and Y (longitude and latitude). Points will appear rotated 90° or in the ocean. If your data looks wrong, check this first.
> 常見錯誤是把 X 與 Y（經度與緯度）弄反，點位會出現在錯誤方位或海上。若資料看起來不對，先檢查這點。

Next: [CRS](crs.md)
