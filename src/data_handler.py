# coding=utf-8
import csv
import Candle


class Cleaner(object):

    @staticmethod
    def clean(csv_file):
        # 读取csv至字典
        reader = csv.reader(csv_file)
        date = csv_file.name.split("_", 2)[1].replace(".csv", "", 1)
        candle = Candle.Candle(date=date)
        # candle.date()
        candle.max_price = 3
        candle.min_price = 99999

        price_index = 7
        current_price = 0
        for item in reader:
            # 忽略第一行
            if reader.line_num == 1:
                continue
            current_price = float(item[price_index])
            if reader.line_num == 2:
                candle.first_price = current_price

            if current_price > candle.max_price:
                candle.max_price = current_price
            if current_price < candle.min_price:
                candle.min_price = current_price

        candle.last_price = current_price
        csv_file.close()
        print(candle)
        return candle


if __name__ == '__main__':
    Cleaner.clean(open("../data/ru主力连续_20170601.csv", "r"))
