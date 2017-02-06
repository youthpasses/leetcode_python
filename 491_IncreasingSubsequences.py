# coding:utf-8
# @makai
# 17/1/6

import itertools

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in xrange(2, len(nums) + 1):
        	res.extend(set(itertools.combinations(nums, i)))
        return [x for x in res if self.isIncreasing(x)]

    def isIncreasing(self, x):
    	for i in xrange(1, len(x)):
    		if x[i - 1] > x[i]:
    			return False
    	return True

print Solution().findSubsequences([1,2,3,3])