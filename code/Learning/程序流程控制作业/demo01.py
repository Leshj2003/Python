# -*-  codeing = utf-8 -*-
# @Time : 2023/3/30 21:14
# @Author : LHJ青梦
# @File : demo01.py
# @Software: PyCharm


def main():
    a,b = map(int,input().split())
    i =0
    while(i <= a):
        if(2 * i + 4 * (a - i) != b):
            i += 1
        else:
            break
    if(i <= a):
        print("有{}只鸡，{}只兔".format(i,a - i))
    else:
        print('Data Error!')

if __name__ == '__main__':
    main()
