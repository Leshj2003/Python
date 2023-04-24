#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/24 10:45
# @Author : LHJ青梦
# @File : 最长公共前缀.py
# @Software: PyCharm

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

# strs = ["flower","flow","flight"]
# tmp=zip(*strs)
# for i in tmp:
#     print(set(i))

# tmp1 = zip('flower','flow','flight')
# for j in tmp1:
#     print(j)


# tem = ('flower','fly','flight','flower')
# print(set(tem))