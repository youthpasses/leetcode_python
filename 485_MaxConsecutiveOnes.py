# coding:utf-8
# @makai
# 17/1/15
###########################

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = res = 0
        nums.append(0)
        for num in nums:
        	if num == 0:
        		res = max(res, l)
        		l = 0
        	else: l += 1
        return res

print Solution().findMaxConsecutiveOnes([1,1,0,1,1,1,1,0])