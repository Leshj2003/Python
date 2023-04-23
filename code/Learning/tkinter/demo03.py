#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/22 21:31
# @Author : LHJ青梦
# @File : demo03.py
# @Software: PyCharm


import tkinter as tk

windows = tk.Tk()
windows.title('Label')
windows.geometry('300x200')

var = tk.StringVar()  # 变量存储器，字体变量存储器是一种用于存储字体变量的设备或组件

l = tk.Label(windows,
             textvariable=var,    # 用textvariable替代text，可以变化
             bg='green',    # 背景颜色
             font=('Arial', 12),    # 字体和字体颜色
             width=15,  # 标签的宽度
             height=2)  # 标签的长度

l.pack()    #固定窗口的位置

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit =True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


b = tk.Button(
    windows,
    text='hit me',
    width=15,
    height=2,
    command=hit_me  # 点击按钮执行命令
)
b.pack()

windows.mainloop()