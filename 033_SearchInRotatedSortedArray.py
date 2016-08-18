# coding:utf-8
# @sinner
# 16/8/17

'''
33. Search in Rotated Sorted Array  QuestionEditorial Solution  My Submissions
Total Accepted: 114766
Total Submissions: 370616
Difficulty: Hard
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question
'''

class Solution(object):
    def search(self, nums, target):
        l = 0; r = len(nums)-1
        while l < r:
            m = (l+r)/2
            if nums[l] <= target and target <= nums[m]: r = m
            elif nums[m+1] <= target and target <= nums[r]: l = m+1
            elif nums[l] > nums[m]: r = m
            else: l = m+1
        if nums[l] == target: return l        
        return -1

print Solution().search([5,6,7,8,9,10,1,2,3,4], 1)