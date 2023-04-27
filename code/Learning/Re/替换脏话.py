#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/26 22:10
# @Author : LHJ青梦
# @File : 替换脏话.py
# @Software: PyCharm

import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)

    print(purified)


if __name__ == '__main__':
    main()