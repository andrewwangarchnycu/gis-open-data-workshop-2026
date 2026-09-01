"""Clean a raw spatial dataset: drop invalid geometry, fix CRS, drop duplicates.

Why 為什麼: mirrors the cleaning steps taught in Lesson 05 and
notebooks/02_geodata_exploration.ipynb, packaged as a reusable script for
data/raw/ -> data/processed/.
對應課程 05 與 notebooks/02_geodata_exploration.ipynb 教授的清理步驟，
包裝為可重複使用的腳本，處理 data/raw/ 至 data/processed/。

Usage 用法:
    python clean_geodata.py --in ../../data/raw/parks.geojson \
        --out ../../data/processed/parks_clean.geojson --crs EPSG:4326
"""
import argparse

import geopandas as gpd


def clean(gdf: gpd.GeoDataFrame, target_crs: str) -> gpd.GeoDataFrame:
    gdf = gdf[gdf.geometry.notnull()].copy()
    gdf = gdf[gdf.geometry.is_valid]
    gdf = gdf.drop_duplicates(subset="geometry")
    if gdf.crs is None:
        raise ValueError("Input layer has no CRS set — set it before cleaning (see qgis/01_basics/crs.md)")
    if str(gdf.crs) != target_crs:
        gdf = gdf.to_crs(target_crs)
    return gdf


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--in", dest="in_path", required=True)
    parser.add_argument("--out", dest="out_path", required=True)
    parser.add_argument("--crs", default="EPSG:4326", help="Target CRS, default EPSG:4326")
    args = parser.parse_args()

    gdf = gpd.read_file(args.in_path)
    before = len(gdf)
    gdf = clean(gdf, args.crs)
    print(f"{before} -> {len(gdf)} features after cleaning")

    gdf.to_file(args.out_path, driver="GeoJSON")
    print(f"Saved to {args.out_path}")


if __name__ == "__main__":
    main()
