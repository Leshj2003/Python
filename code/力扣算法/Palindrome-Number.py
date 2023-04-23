# -*-  coding = utf-8 -*-
# @Time : 2023/4/21 20:54
# @Author : LesHJ0321
# @File : Palindrome-Number.py
# @Software: PyCharm
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]