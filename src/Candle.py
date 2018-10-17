#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Candle(object):

    def __init__(self, date, first_price=0, last_price=0, max_price=0, min_price=0):
        self._date = date
        self._first_price = first_price
        self._last_price = last_price
        self._max_price = max_price
        self._min_price = min_price

    @property
    def date(self):
        return self._date

    @property
    def max_price(self):
        return self._max_price

    @property
    def min_price(self):
        return self._min_price

    @property
    def first_price(self):
        return self._first_price

    @property
    def last_price(self):
        return self._last_price

    @date.setter
    def date(self, date):
        self._date = date

    @max_price.setter
    def max_price(self, max_price):
        self._max_price = max_price

    @min_price.setter
    def min_price(self, min_price):
        self._min_price = min_price

    @first_price.setter
    def first_price(self, first_price):
        self._first_price = first_price

    @last_price.setter
    def last_price(self, last_price):
        self._last_price = last_price

    def __str__(self):
        return "[date=" + self.date + ",min_price=" + str(self.min_price) + ",max_price=" + str(self.max_price) \
               + ",first_price=" + str(self.first_price) + ",last_price=" + str(self.last_price) + "]"
