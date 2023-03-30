# -*-  codeing = utf-8 -*-
# @Time : 2023/1/10 20:16
# @Author : LHJ青梦
# @File : demo10.py
# @Software: PyCharm

#只读模式，报错，打开了一个不存在的文件
# print("-------test---1---")
#
# f = open("123.txt", "r")
#
# print("-------test---2---")       #不会执行

'''

#异常捕获
try:
    print("-------test---1---")

    f = open("123.txt", "r")

    print("-------test---2---")

except IOError:     #文件没找到，属于IO异常（输入输出异常）
    pass    #捕获异常后执行的代码
'''
import time

'''
try:
    print(num)
# except IOError:   #异常类型想要被捕获，需要一致
except NameError:
    print("error")
'''
'''
try:
    print("-------test---1---")

    f = open("test1.txt", "r")

    print("-------test---2---")

    print(num)

except (NameError,IOError):     #将可能的所有异常类型，都放进小括号中
    print("error")
'''
'''
#获取错去描述
try:
    print("-------test---1---")

    f = open("test123.txt", "r")

    print("-------test---2---")

    print(num)

except (NameError,IOError) as result:
    print("error")
    print(result)
'''
'''
#捕获所有的异常
try:
    print("-------test---1---")

    f = open("test1.txt", "r")

    print("-------test---2---")

    print(num)

except Exception as result:     #Exception可以承接所有异常
    print("error")
    print(result)

'''
'''
#try catch 嵌套  finally

try:
    f = open("123.txt", "r")

    try:
        while True:
            content = f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:    #一定会执行
        f.close()
        print("文件关闭")
except Exception as result:
    print("error!")

'''

f = open("gushi.txt", "w", encoding="utf-8")
f.write("静夜思\n李白\n床前明月光\n疑似地上霜\n举头望明月\n低头思故乡")
f = open("gushi.txt", "r", encoding="utf-8")
contents = f.readlines()
print(contents)














