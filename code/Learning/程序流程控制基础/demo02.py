# -*-  codeing = utf-8 -*-
# @Time : 2023/3/29 21:56
# @Author : LHJ青梦
# @File : demo02.py
# @Software: PyCharm

i = 0
while i < 3:
    name = input()
    password = input()
    if password == '666666' and name == 'Kate':
        print('登录成功！')
        break
    else:
        i += 1
        if i == 3:
            print('3次用户名或者密码均有误！退出程序。')
