#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/26 21:22
# @Author : LHJ青梦
# @File : 删除有序数组中的重复项.py
# @Software: PyCharm



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        fast,slow = 0,0;
        lenn = len(nums);
        while fast < lenn:
            if nums[fast] == nums[slow]:
                fast += 1;
            else:
                slow += 1;
                nums[slow] = nums[fast];
        return slow+1

'''
这段代码是一个题目的解法，题目为去除数组中的重复元素，返回去重后的数组长度。
该解法通过快慢指针的方法来实现去重操作。
首先判断数组是否为空，如果为空，则返回0，否则定义两个指针fast和slow，初始化为0。
同时记录数组长度为lenn。接下来进入循环，如果nums[fast]等于nums[slow]，说明存在重复元素，则快指针fast向后移动一位。
否则，说明找到了一个新的元素，慢指针slow向后移动一位，并将新元素赋值给nums[slow]，即将新元素添加到去重后的数组中。
最后返回slow+1，即为去重后的数组长度。 
可以看出，该解法利用了快慢指针的方法，通过移动指针来判断元素是否重复，并将新元素添加到去重后的数组中。
这种方法可以有效地去除数组中的重复元素，并且时间复杂度为O(n)，空间复杂度为O(1)。
'''