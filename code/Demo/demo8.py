# -*-  codeing = utf-8 -*-
# @Time : 2023/1/7 20:28
# @Author : LHJ青梦
# @File : demo8.py
# @Software: PyCharm

'''
#####  函数   #####

def printinfo():
    print("----------")
    print("人生苦短，我用python")
    print("----------")

#函数的调用

printinfo()
'''

'''
#带参数的函数
def add2Num(a, b):
    c = a + b
    print(c)

add2Num(11, 22)
'''
'''
#带返回值的参数
def add2Num(a, b):
    return a + b

result = add2Num(11, 22)
print(result)
#print(add2Num(11,22))
'''
'''
#返回多个值的函数
def divid(a, b):
    shang = a//b
    yushu = a%b
    return shang, yushu

sh, yu = divid(5,2) #需要使用多个值保存返回内容
print("shang:%d yushu:%d"%(sh, yu))

'''
'''
#打印一条横线的函数

def hengxian():
    print("-----------")

hengxian()
'''
###############################
# def printOneLine():
#     print("-"*30)
#
# printOneLine()

'''
#输入参数，打印自定义的横线
def shuru():
    print("-----------")

def shuchu(num):
    i = 0
    while i <num:
        shuru()
        i += 1

print("请输入需要打印的线条数：")
num = int(input())
shuchu(num)
'''
###############################
# def printOneLine():
#     print("-"*30)
#
# def printNumLine(num):
#     i = 0
#     while i <num:
#         printOneLine()
#         i += 1
#
# printNumLine(3)


'''
#求三个数的和
def qiuhe(a,b,c):
    sum = a + b + c
    return sum
print(qiuhe(1,2,3))

'''
###############################
def sum3Number(a,b,c):
    return a+b+c
# print(sum3Number(10,20,30))
# def average3Number(a,b,c):
#     sumResult = sum3Number(10,20,30)
#     averResult = sumResult/3.0
#     return averResult
#
# result = average3Number(10,20,30)
# print("average:%d"%result)

'''
#求三个数的平均值
def qiuhe(a,b,c):
    sum = a + b + c
    return sum


def pingjun():
    sum = qiuhe(1,2,3)
    pj = sum / 3
    return pj
print(pingjun())

'''
'''
#全局变量和局部变量
def test1():
    a = 300     #局部变量:函数内的变量
    print("test1---------修改前:a = %d"%a)
    a = 100
    print("test1---------修改后:a = %d" % a)

def test2():
    a = 500 #不同的函数可以定义相同的名字，彼此无关
    print("test2---------a = %d"%a)

test1()
test2()
'''
'''
#全局变量
a = 100

def test1():
    a = 300     #如果变量一样，则会调用局部优先，就近原则
    print(a)

def test2():
    print(a)    #调用全局变量

test1()
test2()
'''
'''
#在函数中修改全局变量
a = 100

def test1():

    global a    #声明全局变量
    a = 200
    print(a)

def test2():
    print(a)

test1()
test2()
'''
