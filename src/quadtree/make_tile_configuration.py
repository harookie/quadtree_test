from datetime import datetime
import geohash2
import mercantile
import sqlite3
from sqlite3 import Cursor, Connection
from configuration import Configuration
import contextlib


class TileDO:

    def __init__(self, tile: mercantile.Tile):
        self.lv = tile.z
        self.tile_id = mercantile.quadkey(tile)
        self.top_left_x, self.bottom_right_y, self.bottom_right_x, self.top_left_y = mercantile.bounds(tile)
        self.center_x = (self.top_left_x + self.bottom_right_x) / 2
        self.center_y = (self.top_left_y + self.bottom_right_y) / 2
        self.geohash = geohash2.encode(self.center_y, self.center_x, precision=9)


zoom_lv = 21

parent_quadkey = "13211032031020"
parent_tile = mercantile.quadkey_to_tile(parent_quadkey)

configuration: Configuration = Configuration()
cursor: Cursor
db_connection: Connection

s = datetime.now()
with sqlite3.connect('local_db/example.db') as db_connection, \
        contextlib.closing(db_connection.cursor()) as cursor:
    cursor.execute(configuration.CREATE_TILE_INF)

    for t in mercantile.children(parent_tile, zoom=zoom_lv):
        o = TileDO(t)
        cursor.execute(configuration.INSERT_TO_TILE_INF, o.__dict__)

    db_connection.commit()
