# -*-  coding = utf-8 -*-
# @Time : 2023/4/21 20:53
# @Author : LesHJ0321
# @File : Two_Sum.py
# @Software: PyCharm
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            res = target-nums[i]
            if res in nums[i+1:]:
                return [i, nums[i+1:].index(res)+i+1]
                # print([i, nums[i+1:].index(res)+i+1])

nums = eval(input())
target = eval(input())

# print(type(nums))
# print(type(target))

m = Solution()
m.twoSum(nums, target)

