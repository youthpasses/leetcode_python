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
        nums.append(0)
        res = lastLen = currLen = longestLen = 0
        merge = False
        for i, num in enumerate(nums):
        	if num == 1: currLen += 1
        	else:
        		longestLen = max(currLen, longestLen)
        		if nums[i - 1] == 0: lastLen = 0
        		else:
        			if lastLen != 0:
        				res = max(res, lastLen + currLen + 1)
        				merge = True
    	    		lastLen = currLen
    	    		currLen = 0
     	if not merge:
    		if longestLen != len(nums) - 1: return longestLen + 1
    		else: return longestLen
    	return max(res, longestLen + 1)

print Solution().findMaxConsecutiveOnes([1,1,1,0,0])