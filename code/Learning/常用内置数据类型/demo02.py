# -*-  codeing = utf-8 -*-
# @Time : 2023/4/1 10:40
# @Author : LHJ青梦
# @File : demo02.py
# @Software: PyCharm


a = 0
N  = eval(input())
for k in range(1, N+1) :
    a += pow(1 + 1/k, k)*1.0
print("{:.8f}".format(a))
'''

'''