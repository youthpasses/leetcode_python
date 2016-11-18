# coding:utf-8
# @sinner
# 16/11/10

'''
81. Search in Rotated Sorted Array II   QuestionEditorial Solution  My Submissions
Total Accepted: 77414
Total Submissions: 236224
Difficulty: Medium
Contributors: Admin
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0; r = len(nums) - 1
        if nums[0] == nums[-1]:
        	if nums[0] == target: return True
        	else:
        		t = nums[0]
        		while l <= r and nums[l] == t:
        			l += 1
        		while r >= l and nums[r] == t:
        			r -= 1
    	if l > r:
    		return False
        while l < r:
            m = (l + r) / 2
            if nums[l] <= target and target <= nums[m]: r = m
            elif nums[m + 1] <= target and target <= nums[r]: l = m + 1
            elif nums[l] > nums[m]: r = m
            else: l = m + 1
        if nums[l] == target: return True        
        return False

print Solution().search([1, 1, 2], 2)