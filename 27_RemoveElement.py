# coding:utf-8
# @sinner
# 16/6/7

'''
otal Accepted: 122234 Total Submissions: 355979 Difficulty: Easy
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''

'''
too easy
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = 0
        while x < len(nums):
            if nums[x] == val:
                del nums[x]
            else:
                x += 1
        return len(nums)
