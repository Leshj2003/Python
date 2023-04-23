# -*-  codeing = utf-8 -*-
# @Time : 2023/3/28 22:07
# @Author : LHJ青梦
# @File : demo2.py
# @Software: PyCharm


a = input()
if a[0:3] in ['RMB']:
    rmb = eval(a[3:])
    usd = rmb / 6.78
    print("USD{:.2f}".format(usd))
elif a[0:3] in ['USD']:
    usd = eval(a[3:])
    rmb = usd * 6.78
    print("RMB{:.2f}".format(rmb))