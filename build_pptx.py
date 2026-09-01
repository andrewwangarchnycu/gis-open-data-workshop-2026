from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

def add_slide(title, zh_title, bullets):
    """bullets: list of (text, zh_text_or_None, level)"""
    slide = prs.slides.add_slide(blank)

    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.2))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = title
    r.font.size = Pt(32)
    r.font.bold = True

    if zh_title:
        p2 = tf.add_paragraph()
        r2 = p2.add_run()
        r2.text = zh_title
        r2.font.size = Pt(18)

    body_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.8), Inches(12.1), Inches(5.3))
    btf = body_box.text_frame
    btf.word_wrap = True
    first = True
    for text, zh, level in bullets:
        p = btf.paragraphs[0] if first else btf.add_paragraph()
        first = False
        p.level = level
        run = p.add_run()
        run.text = ("• " if level == 0 else "– ") + text
        run.font.size = Pt(20) if level == 0 else Pt(16)
        if zh:
            p2 = btf.add_paragraph()
            p2.level = level
            r2 = p2.add_run()
            r2.text = ("  " if level == 0 else "  ") + zh
            r2.font.size = Pt(14) if level == 0 else Pt(12)
            r2.font.italic = True
    return slide

# 1. Title slide
s = prs.slides.add_slide(blank)
tb = s.shapes.add_textbox(Inches(0.8), Inches(2.4), Inches(11.7), Inches(2.5))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run()
r.text = "Mapping the Unknown"
r.font.size = Pt(44)
r.font.bold = True
p2 = tf.add_paragraph()
r2 = p2.add_run()
r2.text = "GIS, Open Data & Spatial Analysis"
r2.font.size = Pt(24)
p3 = tf.add_paragraph()
r3 = p3.add_run()
r3.text = "探索未知空間：GIS、開放資料與空間分析"
r3.font.size = Pt(20)
p4 = tf.add_paragraph()
r4 = p4.add_run()
r4.text = "A 2-Hour Workshop for Architecture Graduates  ·  建築系畢業生工作坊"
r4.font.size = Pt(16)
r4.font.italic = True

# 2. Mission
add_slide(
    "Project Mission",
    "專案宗旨",
    [
        ("Don't start with a map. Start with a question.", "不要從地圖開始，從問題開始。", 0),
        ("GIS is not only for making maps.", "GIS 不只是用來製圖。", 0),
        ("GIS is a way to think spatially.", "GIS 是一種空間思考方式。", 0),
        ("Research Question → Open Geospatial Data → GIS Exploration → Computational Spatial Analysis → Spatial Insight → Research Map",
         "研究問題 → 開放地理資料 → GIS 探索 → 運算式空間分析 → 空間洞察 → 研究地圖", 0),
    ],
)

# 3. Target audience
add_slide(
    "Target Audience",
    "目標學員",
    [
        ("Architecture graduates and early-stage spatial researchers", "建築系畢業生與初階空間研究者", 0),
        ("Assumes basic architectural / spatial literacy", "假設具備基本建築／空間素養", 0),
        ("No advanced GIS knowledge required", "不需具備進階 GIS 知識", 0),
        ("No advanced Python knowledge required", "不需具備進階 Python 知識", 0),
        ("Taught through architecture, urban space, landscape, public space, environment", "透過建築、都市空間、地景、公共空間、環境案例教學", 0),
    ],
)

# 4. Workshop overview
add_slide(
    "2-Hour Workshop Overview",
    "兩小時工作坊總覽",
    [
        ("01 Mapping the Unknown — 10 min", "01 探索未知空間 — 10 分鐘", 0),
        ("02 From Space to Data — 15 min", "02 從空間到資料 — 15 分鐘", 0),
        ("03 Finding Open Geospatial Data — 15 min", "03 尋找開放地理資料 — 15 分鐘", 0),
        ("04 QGIS Basics — 20 min", "04 QGIS 基礎 — 20 分鐘", 0),
        ("05 Computational GIS with Google Colab — 20 min", "05 使用 Google Colab 的運算式 GIS — 20 分鐘", 0),
        ("06 From Data to Spatial Insight — 15 min", "06 從資料到空間洞察 — 15 分鐘", 0),
        ("07 Research Map Design — 20 min", "07 研究地圖設計 — 20 分鐘", 0),
        ("08 One Map Challenge — 5 min", "08 一張地圖挑戰 — 5 分鐘", 0),
    ],
)

# 5. Module 01
add_slide(
    "01 — Mapping the Unknown (10 min)",
    "01 — 探索未知空間",
    [
        ("What is GIS?", "什麼是 GIS？", 0),
        ("What is spatial thinking?", "什麼是空間思考？", 0),
        ("GIS ≠ map making", "GIS 不等於製圖", 0),
        ("GIS as a research method", "GIS 作為一種研究方法", 0),
    ],
)

# 6. Module 02
add_slide(
    "02 — From Space to Data (15 min)",
    "02 — 從空間到資料",
    [
        ("Core data types: Vector, Raster, Point, Line, Polygon", "核心資料類型：向量、網格、點、線、面", 0),
        ("Attributes, Coordinates, CRS", "屬性、座標、座標參照系統 (CRS)", 0),
        ("Taught using architectural examples", "以建築案例進行教學", 0),
    ],
)

# 7. Module 03
add_slide(
    "03 — Finding Open Geospatial Data (15 min)",
    "03 — 尋找開放地理資料",
    [
        ("Sources: OpenStreetMap, government open data, APIs", "資料來源：OpenStreetMap、政府開放資料、API", 0),
        ("Environmental, transport, and weather data", "環境、交通與氣象資料", 0),
        ("Logic chain:", "邏輯鏈：", 0),
        ("Research Question → Required Variables → Potential Dataset → Data Source → Spatial Dataset",
         "研究問題 → 所需變數 → 潛在資料集 → 資料來源 → 空間資料集", 1),
    ],
)

# 8. Module 04
add_slide(
    "04 — QGIS Basics (20 min)",
    "04 — QGIS 基礎",
    [
        ("Load data / Inspect attributes / Check CRS", "載入資料／檢視屬性／檢查 CRS", 0),
        ("Filter / Buffer / Spatial Join / Intersection", "篩選／緩衝區／空間連結／交集", 0),
        ("Basic symbology", "基礎符號化", 0),
        ("Focus on spatial reasoning, not software commands", "著重空間推理，而非軟體操作指令", 0),
    ],
)

# 9. Module 05
add_slide(
    "05 — Computational GIS with Google Colab (20 min)",
    "05 — 使用 Google Colab 的運算式 GIS",
    [
        ("Tools: Python, GeoPandas, Pandas, Shapely, Matplotlib", "工具：Python、GeoPandas、Pandas、Shapely、Matplotlib", 0),
        ("Workflow: Load → Inspect → Clean → Spatial Operation → Calculate → Visualize",
         "流程：載入 → 檢視 → 清理 → 空間運算 → 計算 → 視覺化", 0),
        ("Beginner-friendly code, runs entirely in Google Colab", "程式碼對初學者友善，完全在 Google Colab 執行", 0),
        ("Every notebook includes an \"Open in Colab\" badge", "每份筆記本皆附「Open in Colab」徽章", 0),
    ],
)

# 10. Module 06
add_slide(
    "06 — From Data to Spatial Insight (15 min)",
    "06 — 從資料到空間洞察",
    [
        ("Chain: Data → Pattern → Relationship → Interpretation → Insight",
         "鏈結：資料 → 模式 → 關係 → 詮釋 → 洞察", 0),
        ("Guiding questions: What? Where? Why? So what?", "引導問題：是什麼？在哪裡？為什麼？所以呢？", 0),
        ("The map is evidence, not the final conclusion", "地圖是證據，而非最終結論", 0),
    ],
)

# 11. Module 07
add_slide(
    "07 — Research Map Design (20 min)",
    "07 — 研究地圖設計",
    [
        ("Visual hierarchy — what should the viewer see first?", "視覺層級——觀者應該先看到什麼？", 0),
        ("Figure-ground, using architectural spatial representation", "圖底關係，運用建築空間再現原則", 0),
        ("Color: Sequential, Diverging, Categorical — color must encode information", "色彩：序列型、發散型、類別型——色彩須承載資訊", 0),
        ("Typography: title, subtitle, legend, annotation, data source, scale, north arrow",
         "字體排印：標題、副標、圖例、註記、資料來源、比例尺、指北針", 0),
        ("Annotation highlights key spatial findings directly on the map", "註記直接標示地圖上的重要空間發現", 0),
        ("Composition: hierarchy, whitespace, alignment, contrast, legibility", "構圖：層級、留白、對齊、對比、可讀性", 0),
        ("Output should look like a research diagram, not a raw GIS screenshot", "成果應呈現為研究圖表，而非原始 GIS 截圖", 0),
    ],
)

# 12. Module 08
add_slide(
    "08 — One Map Challenge (5 min)",
    "08 — 一張地圖挑戰",
    [
        ("Deliverable: 1 Research Question + 1 Spatial Analysis + 1 Research Map + 1 Spatial Insight",
         "成果：1 個研究問題 + 1 項空間分析 + 1 張研究地圖 + 1 個空間洞察", 0),
        ("Example question: Where are the greener public spaces?", "範例問題：哪裡有更綠意的公共空間？", 0),
        ("Possible datasets: Trees, Buildings, Public spaces, Roads", "可能資料集：樹木、建物、公共空間、道路", 0),
        ("Possible analysis: Tree density within public spaces", "可能分析：公共空間內的樹木密度", 0),
        ("Final output includes: Title, Main map, Legend, Data source, Annotation, One key insight",
         "最終成果包含：標題、主地圖、圖例、資料來源、註記、一個關鍵洞察", 0),
    ],
)

# 13. Research case
add_slide(
    "Research Case — Flexible & Transferable",
    "研究案例——彈性且可轉移",
    [
        ("Urban environmental / public-space case with flexible layers", "都市環境／公共空間案例，圖層彈性可調", 0),
        ("Possible layers: buildings, trees, green spaces, roads, public spaces, land use, elevation, environmental observations",
         "可能圖層：建物、樹木、綠地、道路、公共空間、土地使用、高程、環境觀測資料", 0),
        ("NOT hard-coded around thermal comfort", "並非僅侷限於熱舒適度議題", 0),
        ("Transferable to: urban morphology, mobility, walkability, landscape, environmental analysis, public space, architecture, spatial behavior",
         "可轉移應用於：都市型態、移動性、可步行性、地景、環境分析、公共空間、建築、空間行為", 0),
    ],
)

# 14. QGIS + Colab relationship
add_slide(
    "QGIS + Colab Relationship",
    "QGIS 與 Colab 的關係",
    [
        ("QGIS = See the Space", "QGIS = 看見空間", 0),
        ("Colab / Python = Compute the Space", "Colab／Python = 運算空間", 0),
        ("Research Map = Explain the Space", "研究地圖 = 解釋空間", 0),
    ],
)

# 15. Repository structure
add_slide(
    "Repository Structure",
    "儲存庫結構",
    [
        ("README.md, LICENSE, CONTRIBUTING.md", "README.md、LICENSE、CONTRIBUTING.md", 0),
        ("syllabus/ — workshop outline, learning objectives, teaching plan", "syllabus/ — 工作坊大綱、學習目標、教學計畫", 0),
        ("lessons/01–07 — one folder per module", "lessons/01–07 — 每個模組一個資料夾", 0),
        ("notebooks/ — 01_open_data, 02_geodata_exploration, 03_spatial_analysis, 04_mini_research",
         "notebooks/ — 四份 Colab 筆記本", 0),
        ("qgis/ — 01_basics, 02_analysis, 03_map_design", "qgis/ — 基礎、分析、地圖設計", 0),
        ("data/ — raw, processed", "data/ — 原始資料、處理後資料", 0),
        ("scripts/ — download, preprocessing, analysis", "scripts/ — 下載、前處理、分析", 0),
        ("exercises/ — data exploration, QGIS, spatial analysis, one map challenge", "exercises/ — 資料探索、QGIS、空間分析、一張地圖挑戰", 0),
        ("examples/ — research maps, student examples", "examples/ — 研究地圖、學生範例", 0),
        ("resources/ — gis, open-data, python, research-methods, map-design", "resources/ — GIS、開放資料、Python、研究方法、地圖設計", 0),
    ],
)

# 16. Colab requirements
add_slide(
    "Google Colab Requirements",
    "Google Colab 要求",
    [
        ("Every notebook runs in Google Colab with an Open in Colab badge", "每份筆記本皆可在 Google Colab 執行，並附徽章", 0),
        ("Installs dependencies automatically; no local filesystem assumptions", "自動安裝相依套件；不假設本機檔案系統", 0),
        ("Uses small, reproducible datasets", "使用小型、可重現的資料集", 0),
        ("Clear section headers; spatial meaning explained before code", "清楚的段落標題；程式碼前先解釋空間意義", 0),
        ("Includes expected outputs, beginner-friendly comments", "包含預期輸出、對初學者友善的註解", 0),
        ("Ends with a research interpretation exercise", "以研究詮釋練習作結", 0),
        ("Preferred packages: geopandas, pandas, shapely, matplotlib, jupyter, osmnx",
         "偏好套件：geopandas、pandas、shapely、matplotlib、jupyter、osmnx", 0),
    ],
)

# 17. Research Map Design System
add_slide(
    "Research Map Design System",
    "研究地圖設計系統",
    [
        ("Checklist: does the map answer a question? Is the pattern obvious?", "檢核表：地圖是否回答問題？模式是否明顯？", 0),
        ("Clear visual hierarchy, meaningful color encoding, readable typography", "清楚的視覺層級、有意義的色彩編碼、易讀的字體排印", 0),
        ("Unnecessary information removed; study area clear; data source documented", "移除多餘資訊；研究範圍清楚；標註資料來源", 0),
        ("Key insight visible on the map", "地圖上的關鍵洞察清晰可見", 0),
        ("Supporting docs: visual-hierarchy, color-for-maps, typography, figure-ground, annotation, legend-design",
         "支援文件：視覺層級、地圖色彩、字體排印、圖底關係、註記、圖例設計", 0),
    ],
)

# 18. Final map output
add_slide(
    "Final Map Output",
    "最終地圖成果",
    [
        ("Layout: Title / Research Question / Subtitle", "版面：標題／研究問題／副標", 0),
        ("Main map showing the spatial pattern", "呈現空間模式的主地圖", 0),
        ("Legend and Key Insight side by side", "圖例與關鍵洞察並列", 0),
        ("Footer: Data Source · Scale · North · Author", "頁尾：資料來源．比例尺．指北針．作者", 0),
        ("Format: A4 landscape or 16:9", "格式：A4 橫向或 16:9", 0),
        ("Inspired by architectural diagrams, scientific visualization, contemporary cartography, urban analysis graphics",
         "靈感來自建築圖表、科學視覺化、當代製圖學、都市分析圖", 0),
        ("Avoid decorative design that reduces analytical clarity", "避免降低分析清晰度的裝飾性設計", 0),
    ],
)

# 19. Pedagogical principle
add_slide(
    "Pedagogical Principle",
    "教學原則",
    [
        ("Every technical operation must answer: Why are we doing this?", "每個技術操作都必須回答：我們為什麼要這麼做？", 0),
        ("Not: \"Click Buffer.\"", "不是：「點選緩衝區。」", 0),
        ("Instead: \"We create a 10 m buffer to ask which buildings are within 10 m of vegetation.\"",
         "而是：「我們建立 10 公尺緩衝區，是為了詢問哪些建物位於植栽 10 公尺範圍內。」", 0),
        ("Chain: Tool → Spatial Meaning → Research Question", "鏈結：工具 → 空間意義 → 研究問題", 0),
    ],
)

# 20. Quality standard / closing
add_slide(
    "Quality Standard",
    "品質標準",
    [
        ("The repository should feel like Architecture + GIS + Computational Research + Information Design",
         "儲存庫應體現：建築 + GIS + 運算研究 + 資訊設計", 0),
        ("Not a generic programming tutorial", "而非通用程式教學", 0),
        ("Priorities: research thinking, spatial reasoning, data literacy, reproducibility, visual communication, technical implementation",
         "優先順序：研究思維、空間推理、資料素養、可重現性、視覺傳達、技術實作", 0),
        ("Usable as a 2-hour instructor-led workshop and a self-learning research toolkit",
         "可作為兩小時講師帶領工作坊，也可作為自學研究工具包", 0),
    ],
)

# 21. Closing statement
s = prs.slides.add_slide(blank)
tb = s.shapes.add_textbox(Inches(0.8), Inches(2.6), Inches(11.7), Inches(2.5))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run()
r.text = "Map the Unknown → Analyze the Space → Discover the Insight"
r.font.size = Pt(30)
r.font.bold = True
p2 = tf.add_paragraph()
r2 = p2.add_run()
r2.text = "探索未知 → 分析空間 → 發現洞察"
r2.font.size = Pt(20)
p3 = tf.add_paragraph()
r3 = p3.add_run()
r3.text = "\"I can start with a spatial question, find data, analyze it, and communicate what I discovered through a well-designed research map.\""
r3.font.size = Pt(16)
r3.font.italic = True

out_path = "Mapping_the_Unknown_Workshop.pptx"
prs.save(out_path)
print("Saved:", out_path)
