"""Download a small OpenStreetMap extract for a place, via osmnx.

Why 為什麼: gives learners a real open-data download path that mirrors
Lesson 03 (Finding Open Geospatial Data), separate from the notebooks'
inline sample data so the QGIS-facing workflow has a real source too.
提供學習者一個真實的開放資料下載路徑，對應課程 03（尋找開放地理資料），
與筆記本內建範例資料分開，讓面向 QGIS 的工作流程也有真實資料來源。

Usage 用法:
    python download_osm_data.py --place "Da'an District, Taipei, Taiwan" \
        --tags leisure=park --out ../../data/raw/parks.geojson
"""
import argparse
import json

import osmnx as ox


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--place", required=True, help="Place name, e.g. 'Da'an District, Taipei, Taiwan'")
    parser.add_argument("--tags", required=True, help="OSM tag as key=value, e.g. leisure=park")
    parser.add_argument("--out", required=True, help="Output GeoJSON path")
    args = parser.parse_args()

    key, value = args.tags.split("=", 1)
    gdf = ox.features_from_place(args.place, tags={key: value})
    gdf = gdf[gdf.geometry.notnull()]

    gdf.to_file(args.out, driver="GeoJSON")
    print(f"Saved {len(gdf)} features to {args.out}")


if __name__ == "__main__":
    main()
