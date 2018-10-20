# coding=utf-8
from __future__ import unicode_literals
from pyecharts import Kline

from repository import SQLiteUtil


class DataShow(object):
    @staticmethod
    def create_view():
        # open, close, lowest, highest]
        v1 = []
        kline = Kline("日K线图")
        rows = SQLiteUtil.select_all()
        down_flag = []
        for row in rows:
            down_flag.append(row[1])
            v1.append([row[4], row[5], row[2], row[3]])
        kline.add(
            "日K",
            down_flag,
            v1,
            mark_point=["max"],
            is_datazoom_show=True,
        )
        kline.render(path="../view/day.html")

        v1 = []
        kline = Kline("7天K线图")
        rows = SQLiteUtil.select_group_by_week()
        down_flag = []
        for row in rows:
            down_flag.append(row.get("week_flag"))
            v1.append([row.get("first_price"), row.get("last_price"), row.get("min_price"), row.get("max_price")])
        kline.add(
            "周K",
            down_flag,
            v1,
            mark_point=["max"],
            is_datazoom_show=True,
        )
        kline.render(path="../view/week.html")

        v1 = []
        kline = Kline("30天K线图")
        rows = SQLiteUtil.select_group_by_moon()
        down_flag = []
        for row in rows:
            down_flag.append(row.get("moon_flag"))
            v1.append([row.get("first_price"), row.get("last_price"), row.get("min_price"), row.get("max_price")])
        kline.add(
            "月K",
            down_flag,
            v1,
            mark_point=["max"],
            is_datazoom_show=True,
        )
        kline.render(path="../view/moon.html")
