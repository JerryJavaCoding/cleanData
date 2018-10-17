#!/usr/bin/python

import sqlite3

from src.Candle import Candle


class SQLiteUtil(object):
    @staticmethod
    def insert(candle):
        db_conn = sqlite3.connect('../data/candle.db')
        cursor = db_conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tb_candle
               (ID                  INTEGER PRIMARY KEY    AUTOINCREMENT,
               date_str             TEXT    NOT NULL,
               min_price            REAL    NOT NULL,
               max_price            REAL     NOT NULL,
               first_price          REAL     NOT NULL,
               last_price           REAL     NOT NULL);''')
        print "Table created successfully"

        insert_sql = "INSERT INTO tb_candle (date_str,min_price,max_price,first_price,last_price) \
              VALUES ('%s',%s,%s,%s,%s)" % (
            candle.date, candle.min_price, candle.max_price, candle.first_price, candle.last_price)

        cursor.execute(insert_sql)
        print "insert successfully"
        db_conn.commit()
        db_conn.close()

    @staticmethod
    def selectAll():
        db_conn = sqlite3.connect('../data/candle.db')
        cursor = db_conn.cursor()
        rows = cursor.execute("SELECT * FROM tb_candle")
        for row in rows:
            print row


if __name__ == '__main__':
    # candle = Candle('2222', 1, 1, 1, 1)
    # SQLiteUtil.insert(candle)
    SQLiteUtil.selectAll()
