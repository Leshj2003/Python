# -*-  coding = utf-8 -*-
# @Time : 2023/4/21 20:55
# @Author : LesHJ0321
# @File : RomanToInt.py
# @Software: PyCharm
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        str_list=[]
        str_list.extend(s)
        for i, roma in enumerate(str_list):
            if i <(len(str_list)-1) and a[roma] < a[str_list[i+1]]:
                ans -= a[roma]
            else:
                ans += a[roma]
        return ans