import sqlite3
from sqlite3 import Cursor, Connection
import contextlib

from com.skt.tango.analyze.quadtree_test.configuration import Configuration


class KpiConfiguration:

    def __init__(self, kpi_name, vendor, lv, threshold):
        self.kpi_name = kpi_name
        self.vendor = vendor
        self.lv = lv
        self.threshold = threshold


configuration: Configuration = Configuration()
cursor: Cursor
db_connection: Connection

with sqlite3.connect('local_db/example.db') as db_connection, \
        contextlib.closing(db_connection.cursor()) as cursor:
    cursor.execute(configuration.CREATE_KPI_INF)

    kpi_name = "user_count"
    vendor = "ELG"
    threshold = 100

    for lv in range(10):
        o = KpiConfiguration(kpi_name, vendor, lv, threshold*lv)
        cursor.execute(configuration.INSERT_TO_KPI_INF, o.__dict__)

    db_connection.commit()
