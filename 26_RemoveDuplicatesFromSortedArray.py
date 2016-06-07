# coding:utf-8
# @sinner
# 16/6/7

'''
Total Accepted: 134640 Total Submissions: 398464 Difficulty: Easy
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

'''
too easy
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        while len(nums) - 1 >= x + 1:
            if nums[x] == nums[x + 1]:
                del nums[x + 1]
            else:
                x += 1
        return len(nums)