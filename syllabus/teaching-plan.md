# Teaching Plan 教學計畫

Minute-by-minute instructor guide. Adjust pacing to group size and prior exposure to GIS.
逐分鐘教學指引，可依組別大小與 GIS 先備經驗調整節奏。

## 01 — Mapping the Unknown (10 min)

| Min | Activity |
|---|---|
| 0–3 | Open with a spatial question relevant to the room (e.g. "Where in this city would you feel unsafe walking at night, and why?"). Do not mention GIS yet. |
| 3–7 | Reveal: this question already implies data, location, and relationships — that's spatial thinking. Introduce GIS as a research method. |
| 7–10 | Show the pipeline diagram (Research Question → ... → Research Map). State the workshop philosophy: "Don't start with a map. Start with a question." |

引導提問（3 分）→ 揭示空間思考本質（4 分）→ 展示工作流程圖與工作坊理念（3 分）。

## 02 — From Space to Data (15 min)

| Min | Activity |
|---|---|
| 0–5 | Vector vs raster using a building footprint (vector) vs a satellite image (raster). |
| 5–10 | Point/line/polygon via architecture: a tree (point), a street (line), a building footprint (polygon). |
| 10–13 | Attributes: show an attribute table for building footprints (height, use, year). |
| 13–15 | CRS: brief conceptual explanation — "a shared coordinate language" — using a mismatched-layers example. |

Reference: [`lessons/02-space-to-data/`](../lessons/02-space-to-data/)

## 03 — Finding Open Geospatial Data (15 min)

| Min | Activity |
|---|---|
| 0–5 | Show OpenStreetMap + a national open data portal side by side. |
| 5–10 | Walk through the logic: Research Question → Required Variables → Potential Dataset → Data Source → Spatial Dataset, using a live example. |
| 10–15 | Group exercise: learners propose one dataset for their own question of interest. |

Reference: [`lessons/03-open-geospatial-data/`](../lessons/03-open-geospatial-data/)

## 04 — QGIS Basics (20 min)

| Min | Activity |
|---|---|
| 0–3 | Load data (GeoJSON, CSV with lat/lon). |
| 3–6 | Inspect attributes, check CRS. |
| 6–9 | Filter by attribute (e.g. buildings with height > 20m). |
| 9–13 | Buffer — explain *why* (e.g. 10m buffer around vegetation). |
| 13–17 | Spatial join and intersection. |
| 17–20 | Basic symbology (graduated color by attribute). |

Every step: **Tool → Spatial Meaning → Research Question**. Reference: [`qgis/`](../qgis/)

## 05 — Computational GIS with Colab (20 min)

| Min | Activity |
|---|---|
| 0–2 | Open Colab notebook, run install cell. |
| 2–6 | Load + inspect a GeoDataFrame. |
| 6–10 | Clean data (drop nulls, reproject CRS). |
| 10–15 | Spatial operation (buffer/join) in GeoPandas — same operation just done in QGIS. |
| 15–18 | Calculate a metric (e.g. count of trees per public space). |
| 18–20 | Visualize with Matplotlib. |

If time and group comfort allow, swap step 10–18 for [`case-studies/01-green-coverage-grid/`](../case-studies/01-green-coverage-grid/), which runs the same pipeline on real Taipei tree data (no registration needed) — a stronger "this is real" moment than the abstract sample, at the cost of a less predictable dataset shape.
若時間與班級狀況允許，10–18 分鐘的步驟可換成 [`case-studies/01-green-coverage-grid/`](../case-studies/01-green-coverage-grid/)，以真實台北樹木資料執行相同流程（無需申請帳號）——比抽象範例更有「這是真的」的說服力，但資料形狀較不可預期。

Reference: [`notebooks/`](../notebooks/) and [`lessons/05-computational-gis/`](../lessons/05-computational-gis/)

## 06 — From Data to Spatial Insight (15 min)

| Min | Activity |
|---|---|
| 0–5 | Show the computed result from module 05. Ask: "What pattern do you see?" |
| 5–10 | Push through What → Where → Why → So what as a group discussion. |
| 10–15 | Emphasize: the map/chart is evidence for an argument, not the final answer. |

## 07 — Research Map Design (20 min)

| Min | Activity |
|---|---|
| 0–4 | Visual hierarchy — what should the eye see first? |
| 4–8 | Figure-ground, using architectural drawing conventions. |
| 8–12 | Color: sequential vs diverging vs categorical — color must encode information. |
| 12–16 | Typography and required elements: title, legend, scale, north arrow, source. |
| 16–20 | Annotation and composition; quick critique of example maps in `examples/research_maps/`. |

## 08 — One Map Challenge (5 min)

| Min | Activity |
|---|---|
| 0–2 | Restate the deliverable: 1 question + 1 analysis + 1 map + 1 insight. |
| 2–5 | Point learners to `exercises/04_one_map_challenge/` and the design checklist. Set a follow-up deadline if this is a take-home finish. |
