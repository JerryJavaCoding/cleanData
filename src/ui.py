#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import filedialog

from data_handler import Cleaner
from repository import SQLiteUtil


def open_files():
    csv_name = filedialog.askopenfilename(title='打开csv文件', filetypes=[('csv文件', '*.csv')])
    print(csv_name)
    with open(csv_name, 'r') as csv_file:  # 打开文件
        candle = Cleaner.clean(csv_file)
        SQLiteUtil.insert(candle)


root = tkinter.Tk()
btn1 = tkinter.Button(root, text='打开csv文件', font=("宋体", 20, 'bold'), width=13, height=8, command=open_files)

btn1.pack(side='left')

root.mainloop()
