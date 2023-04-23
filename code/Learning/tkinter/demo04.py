#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/22 21:43
# @Author : LHJ青梦
# @File : demo04.py
# @Software: PyCharm

import tkinter as tk

windows = tk.Tk()
windows.title('Entry')
windows.geometry('200x200')

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)

# 输入框,用户输入的内容都显示*
e = tk.Entry(windows, show='*')
e.pack()
# 创建按钮分别触发两种情况
b1 = tk.Button(windows,text='insert point',width=15,height=2,command=insert_point)
b1.pack()
b2 = tk.Button(windows,text='insert end',command=insert_end)
b2.pack()
# 创建文本框
t = tk.Text(windows,height=2)
t.pack()

windows.mainloop()
