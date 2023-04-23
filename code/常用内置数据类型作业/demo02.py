# -*-  codeing = utf-8 -*-
# @Time : 2023/4/1 17:02
# @Author : LHJ青梦
# @File : demo02.py
# @Software: PyCharm

#计算时间差
from datetime import datetime

# 获取用户输入的两个时间字符串
time_str1, time_str2 = input("请输入两个时间字符串，用逗号分隔：").split(',')

# 将时间字符串转换为 datetime 对象
time1 = datetime.strptime(time_str1, '%Y年%m月%d日%H点%M分%S秒')
time2 = datetime.strptime(time_str2, '%Y年%m月%d日%H点%M分%S秒')

# 计算两个 datetime 对象的差值
delta = abs(time2 - time1)

# 输出相差的完整天数
print(delta.days)
