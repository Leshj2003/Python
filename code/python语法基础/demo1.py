# -*-  codeing = utf-8 -*-
# @Time : 2023/3/28 21:22
# @Author : LHJ青梦
# @File : demo1.py
# @Software: PyCharm

'''
该程序首先使用 input() 函数获取输入的温度字符串，
然后判断输入的是摄氏度还是华氏度。如果是摄氏度，
则按照转换公式 F = C * 1.8 + 32 将摄氏度转换为华氏度，
并使用 format() 函数保留两位小数输出。
如果是华氏度，则按照转换公式 C = (F - 32) / 1.8 将华氏度转换为摄氏度，
并同样使用 format() 函数保留两位小数输出。
最终的输出格式为大写字母 C 或 F 开头的温度字符串。
'''
temp_str = input()
if temp_str[0] in ['C']:
    # 摄氏度转换为华氏度
    celsius = eval(temp_str[1:])
    fahrenheit = celsius * 1.8 + 32
    print("F{:.2f}".format(fahrenheit))
elif temp_str[0] in ['F']:
    # 华氏度转换为摄氏度
    fahrenheit = eval(temp_str[1:])
    celsius = (fahrenheit - 32) / 1.8
    print("C{:.2f}".format(celsius))
