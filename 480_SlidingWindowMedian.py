#
# coding:utf-8
# @makai
# 17/1/8
#
############################

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res = []
        a = sorted(nums[:k])
        if k % 2 == 0: res.append((a[k/2 - 1] + a[k/2]) / 2.)
        else: res.append(float(a[k/2]))
        for i in xrange(1, len(nums) - k + 1):
        	a.remove(nums[i - 1])
        	a = self.insertNum(a, nums[i+k-1])
        	if k % 2 == 0: res.append((a[k/2 - 1] + a[k/2]) / 2.)
        	else: res.append(float(a[k/2]))
        return res
    def insertNum(self, a, num):
    	if not a: return [num]
    	if num >= a[-1]: return a + [num]
    	if num <= a[0]: return [num] + a
    	s = 0
    	e = len(a) - 1
    	while s <= e:
    		m = (s + e) / 2
    		if num > a[m]: s = m + 1
    		else: e = m - 1
    	a.insert(s, num)
    	return a

print Solution().medianSlidingWindow([7,0,3,9,9,9,1,7,2,3], 6)
# print Solution().insertNum([1, 3, 5,7,9, 9, 9], 5)
