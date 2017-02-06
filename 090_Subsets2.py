# coding:utf-8
# @makai
# 16/12/22

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        res = [[], nums]
        for x in xrange(1, len(nums)):
        	sets = []
        	self.bt([], sets, nums, x, 0, 0)
        	res += sets
        return res

    def bt(self, subset, sets, nums, x, index, begin):
    	if index == x:
    		subset.sort()
    		if subset not in sets: sets.append(subset)
    		return
    	for i in xrange(begin, len(nums)):
    		self.bt(subset + [nums[i]], sets, nums, x, index + 1, i + 1)

print Solution().subsetsWithDup([])