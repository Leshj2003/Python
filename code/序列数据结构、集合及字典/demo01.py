# -*-  codeing = utf-8 -*-
# @Time : 2023/4/9 10:25
# @Author : LHJ青梦
# @File : demo01.py
# @Software: PyCharm


# 请在...补充一行或多行代码

'''
获取以逗号分隔的多个数据输入（输入为一行），计算基本统计值（平均值、标准差、中位数）

'''

# CalStatisticsV1.py
def getNum():  # 获取用户不定长度的输入
    s = input()
    n = s.split(",")
    return n


def mean(numbers):  # 计算平均值
    sum = 0
    for i in range(len(numbers)):
        num = eval(numbers[i])
        sum += num
    # print(sum)
    mean = sum / len(n)
    return mean


def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    n.sort()
    if len(n) % 2:
        numbers = n[len(n) // 2]
    else:
        num = int(n[len(n) // 2]) + int(n[len(n) // 2 - 1])
        numbers = num / 2

    return numbers

n = getNum()  # 主体函数
m = mean(n)
print(n)
# print(type(n),type(m))
# print("{}".format(median(n)))
# print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n, m), median(n)))

# 1,3,6,9,2,5,1
# 1,1,2,3,5,6,9
# num = int(n[len(n) // 2]) + int(n[len(n) // 2 - 1])
# print(num)
'''
s = input()
lst = s.split(",")
print(lst)
'''
# numbers = eval(lst[1])
# print(type(numbers))

# i = 0
# sum = 0
# if i < len(lst)+1:
#     numbers = eval(lst[i])
#     sum += numbers
# else:
#     mean = sum / len(lst)
#     print(mean)
'''
sum = 0
for i in range(len(lst)):
    numbers = eval(lst[i])
    sum += numbers
print(sum)
mean = sum / len(lst)
print(mean)
'''
# numbers = eval(lst[i])
# sum += numbers
# print(sum)

# print(type(len(lst)))
# print(len(lst))


