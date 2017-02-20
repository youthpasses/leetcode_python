# coding:utf-8
# @makai
# 17/2/19

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {0:-1}
        s = 0
        maxLen = 0
        for i, x in enumerate(nums):
            s += x if x==1 else -1
            if s in dic:
            	maxLen = max(maxLen, i - dic[s])
            else:
            	dic[s] = i
        return maxLen

print Solution().findMaxLength([1,0,1,0,1,1,1,0,0])