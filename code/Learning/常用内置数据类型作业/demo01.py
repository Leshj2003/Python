# -*-  codeing = utf-8 -*-
# @Time : 2023/4/1 12:06
# @Author : LHJ青梦
# @File : demo01.py
# @Software: PyCharm


# x = eval(input())
# if (type(x) == type(1)):
#     print("{:.4f}".format(pow(1/x,x)))
# elif(type(x) != type(1)):
#     print("请输入一个数字")

'''
从用户输入一个数字x，计算并输出(1/x)的x次幂，保留小数点后4位。

要考虑输入异常，如果输入非数字，输出提示：请输入数字；如果运算不正确，输出提示: 运算异常。
'''

try:
    x = float(input())
    result = (1/x)**x
    print("{:.4f}".format(result))
except ValueError:
    print("请输入数字")
except ZeroDivisionError:
    print("运算异常")
except Exception:
    print("运算异常")
