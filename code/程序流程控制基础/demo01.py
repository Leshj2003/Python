# -*-  coding = utf-8 -*-
# @Time : 2023/3/29 21:31
# @Author : LHJ青梦
# @File : demo01.py
# @Software: PyCharm


for i in range(1000,10000):
    a = i // 1000
    b = (i % 1000) // 100
    c = (i % 100) // 10
    d = i % 10
    num = pow(a,4) + pow(b,4) + pow(c,4) + pow(d,4)
    if num == i:
        print(i)


# i = eval(input())
# a = i // 1000
# b = (i % 1000) // 100
# c = (i % 100) // 10
# d = i % 10
# print(a,b,c,d)


# for item in range(100,1000):
#     a = item % 10	#个位
#     b = item // 10 % 10	#十位
#     c = item // 100	#百位
#     if a ** 3 + b ** 3 + c ** 3 == item:
#         print(item)