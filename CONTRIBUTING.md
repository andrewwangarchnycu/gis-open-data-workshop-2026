# Contributing 貢獻指南

Thanks for improving **Mapping the Unknown**. This is a teaching repository — clarity for beginners matters more than technical cleverness.
感謝你願意改善**探索未知空間**這個教學專案。這是一份教學資源，對初學者的清晰度比技術上的精巧更重要。

## Ways to contribute 貢獻方式

- Fix errors in lessons, notebooks, or QGIS guides 修正課程、筆記本或 QGIS 教學中的錯誤
- Add new open data sources relevant to architecture/urban research 新增與建築／都市研究相關的開放資料來源
- Improve bilingual (EN / 繁中) translations 改善中英雙語翻譯
- Add student example maps to `examples/student_examples/` 將學生範例地圖新增至 `examples/student_examples/`
- Suggest new research case variations (see `README.md` §10) 提出新的研究案例延伸方向

## Ground rules 基本原則

1. **Beginner-first.** Assume no advanced GIS or Python knowledge. Explain *why* before *how*.
   **初學者優先。** 假設讀者沒有進階 GIS 或 Python 知識，先解釋「為什麼」再說「怎麼做」。
2. **Every notebook must run in Google Colab** with no local setup and no hidden file dependencies.
   **每份筆記本都必須能在 Google Colab 執行**，不需本地安裝，也不能有隱藏的檔案相依性。
3. **Keep datasets small and reproducible.** Do not commit large raw datasets — link to sources instead, or add small clipped samples to `data/raw/`.
   **資料集需小而可重現。** 不要提交大型原始資料，改用連結指向來源，或於 `data/raw/` 放置裁切後的小樣本。
4. **Bilingual content**: keep English and 繁體中文 together in the same file (English first, then Chinese), not as separate files, so they stay in sync.
   **雙語內容**：英文與繁體中文並列於同一檔案（先英文後中文），不要分成兩個檔案，以利同步維護。
5. **Design matters.** Research maps should follow `resources/map-design/research-map-checklist.md`.
   **設計很重要。** 研究地圖需符合 `resources/map-design/research-map-checklist.md` 的檢查清單。

## Submitting changes 提交變更

1. Fork the repository and create a branch. 建立分支。
2. Make your changes and test notebooks in Colab. 進行修改並在 Colab 測試筆記本。
3. Open a pull request describing what changed and why. 開啟 PR 並說明變更內容與原因。

## Reporting issues 回報問題

Open a GitHub issue with a clear description, the affected file, and (for notebooks) the Colab error output.
請開立 GitHub issue，清楚描述問題、受影響的檔案，以及（若為筆記本問題）Colab 的錯誤訊息。
