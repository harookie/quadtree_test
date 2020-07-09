## 필요한 라이브러리를 불러옵니다.
from datetime import datetime

import geohash2
from pyspark import SparkContext
import mercantile
import sqlite3
from sqlite3 import Cursor, Connection
from com.skt.tango.analyze.quadtree_test.configuration import Configuration
import contextlib


class TileDO:

    def __init__(self, tile: mercantile.Tile):
        self.lv = tile.z
        self.tile_id = mercantile.quadkey(tile)
        self.top_left_x, self.bottom_right_y, self.bottom_right_x, self.top_left_y = mercantile.bounds(tile)
        self.center_x = (self.top_left_x + self.bottom_right_x) / 2
        self.center_y = (self.top_left_y + self.bottom_right_y) / 2
        self.geohash = geohash2.encode(self.center_y, self.center_x, precision=9)


def test_spark():
    sc = SparkContext(master="local", appName="first app")
    df = sc.parallelize(range(0, 10))
    print(df.collect())
    sc.stop()


# test_spark()

zoom_lv = 21
zoom_lv = 23
parent_quadkey = "13211032031020"
# parent_quadkey = "13211032031020" # 0.7s
# parent_quadkey = "1321103203102" # 2.9s
# parent_quadkey = "132110320310" # 13s
# parent_quadkey = "13211032031" # 3m
# parent_quadkey = "1321103203"
parent_tile = mercantile.quadkey_to_tile(parent_quadkey)

configuration: Configuration = Configuration()
cursor: Cursor
db_connection: Connection

s = datetime.now()
with sqlite3.connect('local_db/example.db') as db_connection, \
        contextlib.closing(db_connection.cursor()) as cursor:
    cursor.execute(configuration.CREATE_TILE_INF)

    # cursor.execute(configuration.SELECT_TILE_INF)

    for tile in mercantile.children(parent_tile, zoom=zoom_lv):
        o = TileDO(tile)
        cursor.execute(configuration.INSERT_TO_TILE_INF, o.__dict__)
        # break
        # print(row)
    db_connection.commit()

print(datetime.now() - s)


# tiles = mercantile.children(parent_tile, zoom=zoom_lv)
# first_tile = tiles[0]
#
# o = TileDO(first_tile)
# print(o.__dict__)

# print(f"len(tiles) : {len(tiles)}")
# print(f"tiles[0] : {tiles[0]}")
# print(f"mercantile.quadkey(tiles[0]) : {mercantile.quadkey(tiles[0])}")
# print(f"{mercantile.bounds(first_tile)}")