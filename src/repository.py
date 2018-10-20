#!/usr/bin/python
# coding=utf-8

import os
import sqlite3


class SQLiteUtil(object):

    @staticmethod
    def insert(candle, current_time):
        db_conn = sqlite3.connect('../data/candle.db')
        cursor = db_conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tb_candle
               (ID                  INTEGER PRIMARY KEY    AUTOINCREMENT,
               date_str             TEXT    NOT NULL,
               min_price            REAL    NOT NULL,
               max_price            REAL     NOT NULL,
               first_price          REAL     NOT NULL,
               week_flag            INTEGER  NOT NULL,
               moon_flag            INTEGER  NOT NULL,
               last_price           REAL     NOT NULL);''')
        print "Table created successfully"

        week_flag = current_time / 7
        moon_flag = current_time / 30
        insert_sql = "INSERT INTO tb_candle (date_str,min_price,max_price,first_price,last_price,week_flag,moon_flag) \
              VALUES ('%s',%s,%s,%s,%s,%s,%s)" % (
            candle.date, candle.min_price, candle.max_price, candle.first_price, candle.last_price, week_flag,
            moon_flag)

        cursor.execute(insert_sql)
        print "insert successfully"
        db_conn.commit()
        db_conn.close()

    @staticmethod
    def select_all():
        db_conn = sqlite3.connect('../data/candle.db')
        cursor = db_conn.cursor()
        rows = cursor.execute("SELECT * FROM tb_candle")
        # db_conn.close()
        return rows

    @staticmethod
    def select_group_by_week():
        db_conn = sqlite3.connect('../data/candle.db')
        cursor = db_conn.cursor()
        cursor.execute(
            "SELECT week_flag,min(min_price),max(max_price) FROM tb_candle GROUP BY week_flag ORDER BY week_flag")
        week_data = cursor.fetchall()
        cursor.execute(
            "SELECT week_flag, first_price FROM tb_candle GROUP BY week_flag HAVING min(ID) ORDER BY ID ")
        first_price_data = cursor.fetchall()
        cursor.execute(
            "SELECT week_flag, last_price FROM tb_candle GROUP BY week_flag HAVING max(ID) ORDER BY ID ")
        last_price_data = cursor.fetchall()
        db_conn.commit()
        db_conn.close()
        index = 0
        result = []
        # print first_price_data[index][1]
        for row in week_data:
            obj = {"week_flag": row[0], "min_price": row[1], "max_price": row[2],
                   "first_price": first_price_data[index][1], "last_price": last_price_data[index][1]}
            result.append(obj)
            index = index + 1
        print result
        return result

    @staticmethod
    def select_group_by_moon():
        db_conn = sqlite3.connect('../data/candle.db')
        cursor = db_conn.cursor()
        cursor.execute(
            "SELECT moon_flag,min(min_price),max(max_price) FROM tb_candle GROUP BY moon_flag ORDER BY moon_flag")
        moon_data = cursor.fetchall()
        cursor.execute(
            "SELECT moon_flag, first_price FROM tb_candle GROUP BY moon_flag HAVING min(ID) ORDER BY ID ")
        first_price_data = cursor.fetchall()
        cursor.execute(
            "SELECT moon_flag, last_price FROM tb_candle GROUP BY moon_flag HAVING max(ID) ORDER BY ID ")
        last_price_data = cursor.fetchall()
        db_conn.commit()
        db_conn.close()
        index = 0
        result = []
        # print first_price_data[index][1]
        for row in moon_data:
            obj = {"moon_flag": row[0], "min_price": row[1], "max_price": row[2],
                   "first_price": first_price_data[index][1], "last_price": last_price_data[index][1]}
            result.append(obj)
            index = index + 1
        print result
        return result

    @staticmethod
    def remove_all():
        if os.path.exists("../data/candle.db"):
            os.remove("../data/candle.db")
        else:
            print 'no such file ../data/candle.db'


if __name__ == '__main__':
    # candle = Candle('2222', 1, 1, 1, 1)
    # SQLiteUtil.insert(candle)
    # SQLiteUtil.remove_all()
    SQLiteUtil.select_group_by_week()
