#!/usr/bin/python
# coding=utf-8


from __future__ import print_function
import os

from Tkinter import *
from data_handler import Cleaner
from data_show import DataShow
from repository import SQLiteUtil


def change_progress(txt):
    progress_txt.set(txt)
    # 一定要执行，否则只会等scan_file执行后才会更新
    progress.update()


def scan_file():
    try:
        # 每次都清理db，防止中途关闭
        SQLiteUtil.remove_all()
        change_progress("正在扫描...")
        root_dir = text_input.get()
        if root_dir is None:
            return
        # root_dir = "/Users/jerryyu/Downloads/橡胶价格数据包"
        sub_dirs = os.listdir(root_dir)
        sub_dirs.sort()
        current_time = 0
        change_progress("正在清洗...")

        for sub_dir in sub_dirs:
            if not sub_dir.startswith("1"):
                continue
            files = os.listdir(root_dir + "/" + sub_dir)
            files.sort()
            for file in files:
                if not os.path.isdir(file):
                    f = open(root_dir + "/" + sub_dir + "/" + file)
                    candle = Cleaner.clean(f)
                    SQLiteUtil.insert(candle, current_time)
                    current_time = current_time + 1
        change_progress("创建视图中...")
        DataShow.create_view()
        SQLiteUtil.remove_all()
        change_progress("完成！")
    except:
        change_progress("执行失败！！！")


root = Tk()
root.title('数据可视化')
root.geometry('500x200')
Label(root, text='目录：').place(x=100, y=5)
text_input = Entry(root)
text_input.pack()
btn1 = Button(root, text='开始扫描目录', font=("宋体", 10, 'bold'), width=10, height=2, command=scan_file)

btn1.pack()
progress_txt = StringVar()
progress = Entry(root, textvariable=progress_txt, bd=0)
progress['state'] = 'readonly'

progress.pack()

root.mainloop()
