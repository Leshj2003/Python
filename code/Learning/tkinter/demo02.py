#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/22 21:26
# @Author : LHJ青梦
# @File : demo02.py
# @Software: PyCharm

import tkinter as tk

windows = tk.Tk()
windows.title('Lable')
windows.geometry('300x200')

l = tk.Label(windows,
             text='OMG',    # 标签的文字
             bg='green',    # 背景颜色
             font=('Arial', 12),    # 字体和字体颜色
             width=15,  # 标签的宽度
             height=2)  # 标签的长度

l.pack()    #固定窗口的位置

windows.mainloop()