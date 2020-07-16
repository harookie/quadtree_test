import drawSvg as draw

from datetime import datetime
import random

import geohash2
import mercantile
from mercantile import Tile
import sqlite3
from sqlite3 import Cursor, Connection
from com.skt.tango.analyze.quadtree_test.configuration import Configuration
from com.skt.tango.analyze.quadtree_test.configuration import LV_COLOR_MAP
import contextlib


def get_rect_prop(tile: Tile):
    return

zoom_lv = 21 - 1

parent_quadkey = "132110320"
parent_quadkey = "1321103203"
parent_quadkey = "1321121200"
# parent_quadkey = "13211032031"
# parent_quadkey = "132110320310"
# parent_quadkey = "1321103203102"
# parent_quadkey = "13211032031020"
print(f"parent_quadkey cnt : {len(parent_quadkey)}")

parent_tile = mercantile.quadkey_to_tile(parent_quadkey)
parent_bound = mercantile.xy_bounds(parent_tile)

# d = draw.Drawing(b.right - b.left, b.top - b.bottom, origin='center', displayInline=False)
d = draw.Drawing(parent_bound.right - parent_bound.left, parent_bound.top - parent_bound.bottom, displayInline=False)
s = set()
st = datetime.now()

for cnt, c in enumerate(mercantile.children(parent_tile, zoom=zoom_lv)):
    child_bound = mercantile.xy_bounds(c)
    x = child_bound.left - parent_bound.left
    y = parent_bound.top - child_bound.top
    # width = child_bound.right - child_bound.left
    # height = child_bound.top - child_bound.bottom
    # s.add((width, height))
    # lv = random.randint(0, 9)
    # d.append(
    #         draw.Rectangle(x, y, width, height, fill=LV_COLOR_MAP[lv], fill_opacity=0.7, stroke_width=0.2, stroke="black"))
    # if cnt > 100:
    #     break

# d.setPixelScale(2)  # Set number of pixels per geometry unit
# d.saveSvg('example.svg')

print(cnt)
print(s)
print(datetime.now()-st)
# {(76.43702828511596, 76.43702828511596)}
# {(76.43702828511596, 76.43702828511596)}
# {(76.43702828511596, 76.43702828511596)}
# {(38.21851414255798, 38.21851414255798)}
# {(19.109257072210312, 19.10925707127899)}