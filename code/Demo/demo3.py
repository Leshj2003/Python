# -*-  codeing = utf-8 -*-
# @Time : 2023/1/2 18:30
# @Author : LHJ青梦
# @File : demo3.py
# @Software: PyCharm
'''
if True:#注意冒号
    print("True")#缩进要求严格，同一代码块
else:
    print("False")
print("end")#范围是在if外的结构
'''

'''
score = 40
if score >= 90 and score <= 100 :
    print("A")
elif score >= 80 and score <90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score <70:
    print("D")
else:
    print("不及格")
'''
'''
sex = 1#1为男，0为女
marry = 1#1为结婚，0为非结婚
if sex == 1:
    print("男")
    if marry == 1:
        print("已结婚")
    else:
        print("6")
else:
    print("女")
    print("....")
'''
'''
#随机数库
import random
x = random.randint(0,2)     #随机生成【0，2】
print(x)
'''
#剪刀0，石头1，布2
#输入0-2
import random

m = int(input("请选择出战手势（剪刀0，石头1，布2）:"))
r = random.randint(0,2)

if m !=0 and m != 1 and m != 2:
    print("请输入正确数字！！")
else:
    print("你的输入为:%d" % m)
    print("机器人出战手势为:%d" % r)
    if m == 1 and r == 0:
        print("你赢了")
    elif m == 0 and r == 2:
        print("你赢了")
    elif m == 2 and r == 1:
        print("你赢了")
    elif m == r:
        print("平手")
    else:
        print("你输了")




