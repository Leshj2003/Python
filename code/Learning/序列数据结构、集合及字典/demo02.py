# -*-  codeing = utf-8 -*-
# @Time : 2023/4/11 9:31
# @Author : LHJ青梦
# @File : demo02.py
# @Software: PyCharm


s = input()
try:
    d = eval(s)
    e = {}
    for k in d:
        # print(k)  #键
        # print(d[k])   #值
        e[d[k]] = k
    print(e)
except:
    print("输入错误")



'''
这段代码实现了一个功能，即将一个字典的键和值互换后输出。

首先，通过input()函数获取用户输入的内容，并存储在变量s中。然后，使用eval()函数将字符串s转换成字典类型d。如果输入的字符串不是合法的字典格式，就会抛出异常并输出“输入错误”。

接着，定义一个新的字典e，用于存储互换后的键值对。使用for循环遍历字典d的键，并将每个键值对中的键值互换后存储到e中。

最后，使用print()函数输出e，即字典中键值互换后的结果。
'''