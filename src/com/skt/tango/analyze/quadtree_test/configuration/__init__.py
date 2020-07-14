LV_COLOR_MAP = {0: "#31353B", 1: "#3B484D", 2: "#445C5D", 3: "#4F726B", 4: "#5E8775", 5: "#719D7D", 6: "#8AB282",
                7: "#A9C687", 8: "#CDD98B", 9: "#F5EB92"}

#1E0D6D,#301886,#43249C,#5632AF,#6B41BF,#7F52CB,#9363D4,#A676D9,#B889DA,#C89ED7,#D7B4CF,#E3CAC3

class Configuration:
    CREATE_TILE_INF = """
CREATE TABLE IF NOT EXISTS TILE_INF
(LV INTEGER, TILE_ID TEXT, GEOHASH TEXT, TOP_LEFT_X REAL, TOP_LEFT_Y REAL, BOTTOM_RIGHT_X REAL, BOTTOM_RIGHT_Y REAL,
 CENTER_X REAL, CENTER_Y REAL)""".strip()

    INSERT_TO_TILE_INF = """
INSERT INTO TILE_INF(LV, TILE_ID, GEOHASH, TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y, CENTER_X, CENTER_Y)
VALUES(:lv, :tile_id, :geohash, :top_left_x, :top_left_y, :bottom_right_x, :bottom_right_y, :center_x, :center_y)""".\
        strip()

    CREATE_KPI_INF = """
CREATE TABLE IF NOT EXISTS KPI_INF
(KPI_NAME TEXT, VENDOR TEXT, LV INTEGER, THRESHOLD REAL)""".strip()

    INSERT_TO_KPI_INF = """
INSERT INTO KPI_INF(KPI_NAME, VENDOR, LV, THRESHOLD)
VALUES(:kpi_name, :vendor, :lv, :threshold)""".strip()

    CREATE_TILE_KPI_INF = """
CREATE TABLE IF NOT EXISTS KPI_INF
(EVENT_TIME, LV, TILE_ID, KPI_VALUE)""".strip()

    INSERT_TO_TILE_KPI_INF = """
INSERT INTO TILE_KPI_INF(EVENT_TIME, LV, TILE_ID, KPI_VALUE)
VALUES(:event_time, :lv, :tile_id, :kpi_value)""".strip()
