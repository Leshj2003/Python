# -*-  codeing = utf-8 -*-
# @Time : 2023/1/10 19:53
# @Author : LHJ青梦
# @File : demo9.py
# @Software: PyCharm

'''
f = open("test.txt", "w")   #w写入,打开文件，w模式，不存在则创建
#不写w，默认有r只读     w若存在会覆盖     a存在则追加，反之       rb，wb，字节方式，二进制
f.write("hello world,i am here!")   #将字符串写入文件

f.close()   #关闭文件
'''

'''
#read方法读取指定的字符开始是定位在文件头部，每执行一次向后一步
f = open("test.txt", "r")

content = f.read(5)

print(content)

content = f.read(5)     #执行一次读取往后移

print(content)

f.close()

'''

'''
f = open("test.txt", "r")

content = f.readlines()     #一次性读取全部文件为列表，每行有一个字符串元素

# print(content)

i = 1

for temp in content:
    print("%d:%s"%(i,temp))
    i += 1

f.close()

'''
'''
f = open("test.txt", "r")

content = f.readline()      #只能读一行

print("1:%s" % content, end="")

content = f.readline()

print("2:%s" % content)

f.close()

'''

# import os
#
# os.rename("test.txt", "test1.txt")




