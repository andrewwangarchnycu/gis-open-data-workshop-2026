# Layout Manager 版面配置管理員

**Why 為什麼**: the Layout Manager is where your GIS canvas becomes a finished research map — with title, legend, scale, and north arrow, following the design principles in [Lesson 07](../../lessons/07-research-map-design/).
版面配置管理員是將 GIS 畫布轉為完整研究地圖之處——包含標題、圖例、比例尺、指北針，遵循[課程 07](../../lessons/07-research-map-design/)的設計原則。

## Steps 步驟

1. `Project → New Print Layout…` 專案 → 新增印刷排版…
2. Name it and choose a size — **A4 landscape** or a custom 16:9 canvas. 命名並選擇尺寸——A4 橫向或自訂 16:9 畫布。
3. `Add Item → Add Map` — drag to draw the main map frame. 新增項目 → 新增地圖，拖曳繪製主要地圖框。
4. Add supporting elements: 新增輔助元素：
   - `Add Item → Add Legend` 圖例
   - `Add Item → Add Scale Bar` 比例尺
   - `Add Item → Add North Arrow` (via the Arrow tool or a north-arrow SVG) 指北針
   - `Add Item → Add Label` for title, subtitle, data source, annotation 標題、副標題、資料來源、標註文字
5. Align elements using the built-in alignment tools (select multiple → right-click → **Align**). 使用內建對齊工具將元素對齊（選取多個項目 → 右鍵 → 對齊）。

![Screenshot placeholder: Print Layout with map frame, legend, scale bar, and title placed](placeholder-layout-manager.png)
*截圖佔位：印刷排版含地圖框、圖例、比例尺與標題*

## Checklist before moving on 進行下一步前的檢查清單

- [ ] Title states the research question, not just a place name. 標題陳述研究問題，而非僅是地名。
- [ ] Legend uses the same terms as your written interpretation. 圖例用語與你的書面詮釋一致。
- [ ] Data source and CRS/scale are visible somewhere on the layout. 資料來源與 CRS／比例尺於版面上可見。

Full design guidance: [`resources/map-design/`](../../resources/map-design/)

Next: [Exporting Maps](exporting-maps.md)
