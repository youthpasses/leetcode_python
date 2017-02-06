# coding:utf-8
# @makai
# 17/1/6

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]																																																				
        :type S: int
        :rtype: int
        """
        s = sum(nums)
        if s < S: return 0
        if (s + S) % 2 > 0: return 0
        s = (s + S) / 2
        dp = {0:1}
        for num in nums:
        	for x in xrange(s, num - 1, -1):
        		dp[x] = dp.get(x, 0) + dp.get(x - num, 0)
        return dp[s]

print Solution().findTargetSumWays([1,2,7,9,981], 1000000000)