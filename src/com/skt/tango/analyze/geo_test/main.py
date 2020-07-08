## 필요한 라이브러리를 불러옵니다.
from pyspark import SparkContext
import mercantile
import sqlite3

"""
sc = SparkContext(master="local", appName="first app")

df = sc.parallelize(range(0, 10))
print(df.collect())
sc.stop()
"""

zoom_lv = 21
parent_quadkey = "13211032031020"
parent_tile = mercantile.quadkey_to_tile(parent_quadkey)
tiles = mercantile.children(parent_tile, zoom=zoom_lv)
first_tile = tiles[0]
print(f"len(tiles) : {len(tiles)}")
print(f"tiles[0] : {tiles[0]}")
print(f"mercantile.quadkey(tiles[0]) : {mercantile.quadkey(tiles[0])}")
print(f"{mercantile.bounds(first_tile)}")
