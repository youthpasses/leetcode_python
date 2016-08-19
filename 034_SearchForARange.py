# coding:utf-8
# @sinner
# 16/8/19

'''
34. Search for a Range  QuestionEditorial Solution  My Submissions
Total Accepted: 95131
Total Submissions: 317692
Difficulty: Medium
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low = 0
        high = len(nums) - 1
        mid = (low + high) / 2
        while nums[mid] != target and low < high:
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) / 2
        if nums[mid] == target:
            l = mid
            r = mid
            while l >= low and nums[l] == target:
                l -= 1
            l += 1
            while r <= high and nums[r] == target:
                r += 1
            r -= 1
            return [l, r]
        else:
            return [-1, -1]

print Solution().searchRange([], 8)





