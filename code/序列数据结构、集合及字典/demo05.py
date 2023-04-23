# -*-  coding = utf-8 -*-
# @Time : 2023/4/14 19:31
# @Author : LHJ青梦
# @File : demo05.py
# @Software: PyCharm

'''
描述

大学排名没有绝对的公正与权威，附件（alumni.txt, soft.txt）中为按照不同评价体系给出的国内大学前100名排行，对比两个排行榜单前m的学校的上榜情况，分析不同排行榜排名的差异。

根据输入，输出以下内容：

第一行输入1,第二行输入m，输出在alumni.txt和soft.txt榜单中均在前m个记录的大学，按照学校名称升序。

第一行输入2,第二行输入m，输出在alumni.txt或者soft.txt榜单中前m个记录的所有大学，按照学校名称升序。

第一行输入3,第二行输入m，输出出现在榜单alumni.txt中前m个记录但未出现在榜单soft.txt前m个记录中的大学，按照学校名称升序。

第一行输入4,第二行输入m，输出没有同时出现在榜单alumni.txt前m个记录和榜单soft.txt前m个记录的大学，按照学校名称升序。

第一行输入其他数据，则直接输出‘Wrong Option’

'''

#本题要求读取前m个记录，因为almun文件中武大与天津大学均排名前10，不要使用文件中序号选取数据！！
def read_file(file,m):
    """读文件中的学校名到列表中，返回排名前m学校集合"""
    with open(file, "r", encoding="utf-8") as data:
        university_list = [line.strip().split()[1] for line in data]
    return set(university_list[:m])


def either_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在这两个排行榜中均名列前m的学校名，按照学校名称排序，
    返回排序后的列表
    """
    either_set = alumni & soft  #交集
    return sorted(list(either_set))




def all_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在两个榜单中名列前m的所有学校名，按照学校名称排序，
    返回排序后的列表
    """
    all_in_set = alumni | soft  #并集
    return sorted(list(all_in_set))


def only_alumni(alumni, soft):
    """接收两个排行榜前10高校名字集合，
    获得在alumni榜单中名列前10但soft榜单中未进前10的学校名，
    按照学校名称排序，返回排序后的列表
    """
    only_alumni_set = alumni - soft #差集
    return sorted(list(only_alumni_set))


def only_once(alumni, soft):
    """接收两个排行榜前10高校名字集合，
    获得在alumni和soft榜单中名列前10，但不同时出现在两个榜单的学校名，
    按照学校名称排序，返回排序后的列表
    """
    only_once_set = alumni ^ soft   #对称差集
    return sorted(list(only_once_set))


if __name__ == '__main__':
    n=input()
    if n in '1234':
        m=int(input())
        alumni_set = read_file('./alumni.txt',m)
        soft_set = read_file('./soft.txt',m)
        if n=='1':
            either_rank = either_in_top(alumni_set, soft_set)
            print(f'两榜单中均名列前{m}的学校：')
            print(either_rank)
        elif n=='2':
            all_rank = all_in_top(alumni_set, soft_set)
            print(f'两榜单名列前{m}的所有学校：')
            print(all_rank)
        elif n=='3':
            only_in_alumni_rank = only_alumni(alumni_set, soft_set)
            print(f'alumni中名列前{m}，soft中未进前{m}的学校：')
            print(only_in_alumni_rank)
        elif n=='4':
            alumni_soft_rank = only_once(alumni_set, soft_set)
            print(f'不同时出现在两个榜单前{m}的学校：')
            print(alumni_soft_rank)
    else:
        print('Wrong Option')



    # with open('./alumni.txt', "r", encoding="utf-8") as data:
    #     print(data.read())

    # r = read_file('./alumni.txt',10)
    # print(r)

