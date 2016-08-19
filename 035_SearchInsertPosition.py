# coding:utf-8
# @sinner
# 16/8/19

'''
35. Search Insert Position  QuestionEditorial Solution  My Submissions
Total Accepted: 118193
Total Submissions: 310291
Difficulty: Medium
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        l = 0
        r = len(nums) - 1
        m = (l + r) / 2
        while l <= r:
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
            m = (l + r) / 2
        if m == -1:
            return 0
        return m if nums[m] > target else m + 1

print Solution().searchInsert([1, 3, 5, 6], 2)









