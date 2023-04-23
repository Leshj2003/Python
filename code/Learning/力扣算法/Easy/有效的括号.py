#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/23 20:04
# @Author : LHJ青梦
# @File : 有效的括号.py
# @Software: PyCharm


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c  in s:
            if c in d:
                stack.append(d[c])
            else:
                if stack != [] and stack[-1] == c:
                    stack.pop()
                else:
                    return False

        return stack == []