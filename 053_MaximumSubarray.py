# coding:utf-8
# @sinner
# 16/9/3

'''
53. Maximum Subarray  QuestionEditorial Solution  My Submissions
Total Accepted: 130996
Total Submissions: 348584
Difficulty: Medium
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        s = nums[0]
        res = s
        for x in xrange(1, len(nums)):
            s = max(nums[x], s + nums[x])
            res = max(res, s)
        return res

print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])




