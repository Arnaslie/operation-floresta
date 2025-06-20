#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 16:47:22 2025

@author: hereagain
"""

import geopandas as gpd
from shapely.ops import nearest_points
from shapely.ops import unary_union
import fiona
root = "/Users/hereagain/Desktop/OpenAItoZ/dataset/test/riverdistance"
print("geopandas version   :", gpd.__version__)
print("Fiona    ", fiona.__version__)

root = "/Users/hereagain/Desktop/OpenAItoZ/dataset/test/riverdistance"

sites = gpd.read_file("/Users/hereagain/Desktop/OpenAItoZ/dataset/test/riverdistance/candidate_sites_utm.shp")
print("Loaded", len(sites), "features")

#rivers = gpd.read_file(f"{root}/xingu_major1_utm.shp")   

def cal_dist(riverfile,colname):
    rivers = gpd.read_file(f"{root}/{riverfile}")
    river_union = unary_union(rivers.geometry) 
    sites[f'{colname}'] = sites.geometry.distance(river_union)
    return sites

#river_union = unary_union(rivers.geometry)    
#sites["dist_major1_m"] = sites.geometry.distance(river_union)

newsites = cal_dist('xingu_major1_utm.shp', 'distriver1')
newsites = cal_dist('xingu_major2_utm.shp', 'distriver2')
newsites.to_csv('/Users/hereagain/Desktop/OpenAItoZ/dataset/UpperXingu_test.csv',index=False)

#sites.to_file(f"{root}/candidate_sites_with_major1_distance.gpkg",
#              layer="sites", driver="GPKG")





#river3  = gpd.read_file(f"{root}/xingu_major3_utm.shp") # blank 





sites_new=cal_dist('xingu_major3_utm.shp', 'dist_major3_m')
    
    
    

# 2️⃣  sp