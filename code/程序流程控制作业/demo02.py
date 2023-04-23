# -*-  codeing = utf-8 -*-
# @Time : 2023/3/30 21:15
# @Author : LHJ青梦
# @File : demo02.py
# @Software: PyCharm


wall = int(input())
a = b = 1
day = 0
time = 1
na, nb = 0, 0
while wall > 0:
    if a+b > wall:
        time = wall / (b + a)
    wall = wall - b - a
    nb += time * b
    na += time * a
    a *= 2
    b *= 0.5
    day += 1
print(day)
print(round(nb, 1), round(na, 1))