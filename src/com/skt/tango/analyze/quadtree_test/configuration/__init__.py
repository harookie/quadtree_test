class Configuration:
    CREATE_TILE_INF = """
CREATE TABLE IF NOT EXISTS TILE_INF
(LV INTEGER, TILE_ID TEXT, GEOHASH TEXT, TOP_LEFT_X REAL, TOP_LEFT_Y REAL, BOTTOM_RIGHT_X REAL, BOTTOM_RIGHT_Y REAL,
 CENTER_X REAL, CENTER_Y REAL)""".strip()

    INSERT_TO_TILE_INF = """
INSERT INTO TILE_INF(LV, TILE_ID, GEOHASH, TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y, CENTER_X, CENTER_Y)
VALUES(:lv, :tile_id, :geohash, :top_left_x, :top_left_y, :bottom_right_x, :bottom_right_y, :center_x, :center_y)""".\
        strip()

    SELECT_TILE_INF = """
SELECT * FROM TILE_INF""".strip()
