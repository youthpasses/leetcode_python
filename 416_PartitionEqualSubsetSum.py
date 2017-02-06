# coding:utf-8
# @makai
# 17/1/6

'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 > 0: return False
        s = s / 2
        dp = {0: True}
        for num in nums:
        	for x in xrange(s, num - 1, -1):
        		dp[x] = dp.get(x, False) or dp.get(x - num, False)
        return dp.get(s, False)

print Solution().canPartition([1,5,11,5])