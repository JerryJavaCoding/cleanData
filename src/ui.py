#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import tkinter

from data_handler import Cleaner
from src.repository import SQLiteUtil


def scan_file():
    root_dir = text_input.get()
    print "dir is:" + root_dir
    if root_dir is None:
        return
    root_dir = "/Users/jerryyu/Downloads/橡胶价格数据包"
    sub_dirs = os.listdir(root_dir)
    sub_dirs.sort()
    current_time = 0
    for sub_dir in sub_dirs:
        files = os.listdir(root_dir + "/" + sub_dir)
        files.sort()
        for file in files:
            if not os.path.isdir(file):
                f = open(root_dir + "/" + sub_dir + "/" + file)
                candle = Cleaner.clean(f)
                SQLiteUtil.insert(candle, current_time)
                current_time = current_time + 1

    # SQLiteUtil.remove_all()


root = tkinter.Tk()
text_input = tkinter.Entry(root)
text_input.pack()
btn1 = tkinter.Button(root, text='打开csv文件', font=("宋体", 10, 'bold'), width=6, height=2, command=scan_file)

btn1.pack()

root.mainloop()
