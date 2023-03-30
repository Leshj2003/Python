# -*-  codeing = utf-8 -*-
# @Time : 2023/3/29 9:39
# @Author : LHJ青梦
# @File : demo4.py
# @Software: PyCharm

'''

i = 100
while i < 1000:
    s = ""
    a = int(i / 100)
    b = int((i / 10) % 10)
    c = int(i % 10)
    num1 = int(pow(a,3) + pow(b,3) + pow(c,3))
    if num1 == i:
        # s = ("{}, ".format(i))
        s += str.format("{}{}{}, ",a,b,c)
        print(s, end='')
        i+=1
    else:
        i+=1
'''


result = [] # 用于存储结果的列表

for num in range(100, 1000):
    # 分离出百位、十位和个位
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    num1 = int(pow(a, 3) + pow(b, 3) + pow(c, 3))
    # 判断是否为水仙花数
    if num == num1:
        result.append(num) # 将水仙花数添加到结果列表中

# 输出结果
print(", ".join(str(num) for num in result))
'''
在上面的代码中，我们使用了一个for循环来遍历所有三位数，
使用整除和取余运算符分离出百位、十位和个位数字，并判断是否为水仙花数。
如果是水仙花数，则将其添加到一个结果列表中，
最后将列表中的结果使用join()方法连接成一个字符串并输出。
'''