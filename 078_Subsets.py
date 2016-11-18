# coding:utf-8
# @sinner
# 16/11/7

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
        	return [[]]
        if n == 1:
        	return [[], nums]
        nn = n / 2
        res = [[], nums]
        for x in xrange(1, nn + 1):
        	subres = []
        	self.bt(subres, x, 0, [], nums)
        	res.extend(subres)
        	if n - x != x:
        		subres_op = [list(set(x) ^ set(nums)) for x in subres]
        		res.extend(subres_op)
        return res

    def bt(self, subres, kk, i, l, nums):
    	if kk == 0:
    		subres.append(l)
    		return
    	for j in xrange(i + 1, len(nums) + 1):
    		self.bt(subres, kk - 1, j, l + [nums[j - 1]], nums)

print Solution().subsets([2,3,4,8,9,0])