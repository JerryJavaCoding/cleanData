# coding=utf-8
from Tkinter import Tk, Button, Entry, StringVar

import tushare as ts
import datetime as dt


def get_today_data():
    today = dt.date.today()
    today_str = today.strftime('%Y-%m-%d')

    finance_data = ts.get_hist_data(code='600848', start=today_str)
    if finance_data.empty:
        txt = '今日无数据'
        progress_txt.set(txt)
        # 一定要执行，否则只会等scan_file执行后才会更新
        progress.update()
        print txt
    else:
        finance_data.to_csv(today_str + '.csv', columns=['open', 'close', 'high', 'low'])
        txt = today_str + '拉取成功'
        print txt
        progress_txt.set(txt)
        # 一定要执行，否则只会等scan_file执行后才会更新
        progress.update()


if __name__ == '__main__':
    root = Tk()
    root.title('每日数据获取')
    root.geometry('300x150')
    btn1 = Button(root, text='拉取数据', font=("宋体", 10, 'bold'), width=10, height=2, command=get_today_data)
    btn1.pack()
    progress_txt = StringVar()
    progress = Entry(root, textvariable=progress_txt, bd=0)
    progress['state'] = 'readonly'
    progress.pack()
    root.mainloop()
