# -*-  codeing = utf-8 -*-
# @Time : 2023/3/31 19:58
# @Author : LHJ青梦
# @File : demo03.py
# @Software: PyCharm


import random
a, b = eval(input())
s = ""
random.seed(a+b)
for i in range(20):
    s += chr(random.randint(32, 127))
print(s)