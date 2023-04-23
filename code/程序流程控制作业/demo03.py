# -*-  codeing = utf-8 -*-
# @Time : 2023/3/30 22:05
# @Author : LHJ青梦
# @File : demo03.py
# @Software: PyCharm


total_cost = float(input())  # total_cost为当前房价
annual_salary = float(input())  # 年薪
portion_saved = float(input()) / 100
# 月存款比例，输入30转为0.30（即30%）
semi_annual_raise = float(input()) / 100
# 输入每半年加薪比例，输入7转化为0.07（即7%）
portion_down_payment = 0.3

#首付比例，浮点数

down_payment = portion_down_payment * total_cost#首付款
print('首付', down_payment)
current_savings = 0

# 存款金额，从0开始
number_of_months = 1

monthly_salary = annual_salary / 12
# 月工资
monthly_deposit = monthly_salary * portion_saved  # 月存款

while True:
    current_savings += 2.25 * 0.01 * current_savings / 12 #上个月的利息
    current_savings = current_savings + monthly_deposit  # 存款

    if number_of_months % 12 == 0:
        print("第{}个月月末有{:,.0f}元存款".format(number_of_months, current_savings))  # 每12个月输出一次存款，保留0位小数，使用千分符

    if current_savings >= down_payment:
        break

    if number_of_months % 6 == 0:
        monthly_deposit = monthly_deposit * (1 + semi_annual_raise)  # 加薪
    number_of_months = number_of_months + 1

print(f'需要{number_of_months}个月可以存够首付')