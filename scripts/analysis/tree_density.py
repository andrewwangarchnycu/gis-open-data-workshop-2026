"""Compute tree density per public space polygon.

Why 為什麼: packages the buffer -> spatial join -> calculate pipeline from
Lesson 04/05 and notebooks/03_spatial_analysis.ipynb as a reusable script,
so the same analysis can run on any trees/public-spaces pair of GeoJSON
files, not just the workshop's inline sample.
將課程 04／05 與 notebooks/03_spatial_analysis.ipynb 中「緩衝區 -> 空間 join
-> 計算」的流程包裝為可重複使用的腳本，讓相同分析可套用於任何一組
樹木／公共空間 GeoJSON 資料，而不僅限於工作坊的內建範例。

Usage 用法:
    python tree_density.py --trees trees.geojson --spaces public_spaces.geojson \
        --metric-crs EPSG:3826 --buffer-m 10 --out density.geojson
"""
import argparse

import geopandas as gpd


def compute_tree_density(trees: gpd.GeoDataFrame, spaces: gpd.GeoDataFrame,
                          metric_crs: str, buffer_m: float) -> gpd.GeoDataFrame:
    trees_m = trees.to_crs(metric_crs)
    spaces_m = spaces.to_crs(metric_crs)

    joined = gpd.sjoin(trees_m, spaces_m, how="left", predicate="within")
    tree_counts = joined.groupby(joined.index_right).size().rename("tree_count")

    spaces_m = spaces_m.join(tree_counts)
    spaces_m["tree_count"] = spaces_m["tree_count"].fillna(0)
    spaces_m["area_m2"] = spaces_m.geometry.area
    spaces_m["tree_density_per_1000m2"] = spaces_m["tree_count"] / spaces_m["area_m2"] * 1000
    return spaces_m


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trees", required=True)
    parser.add_argument("--spaces", required=True)
    parser.add_argument("--metric-crs", default="EPSG:3826")
    parser.add_argument("--buffer-m", type=float, default=10)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    trees = gpd.read_file(args.trees)
    spaces = gpd.read_file(args.spaces)

    result = compute_tree_density(trees, spaces, args.metric_crs, args.buffer_m)
    result.to_file(args.out, driver="GeoJSON")
    print(result[["tree_count", "area_m2", "tree_density_per_1000m2"]])
    print(f"Saved to {args.out}")


if __name__ == "__main__":
    main()
