# coding:utf-8
# @makai
# 16/12/18


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = {}
        count = len(nums)
        for num in nums:
            b = bin(num)[2:]
            for x in xrange(1, len(b) + 1):
                c = b[-x]
                if c == '1':
                    ones[x] = ones.get(x, 0) + 1
        res = 0
        for k in ones.keys():
            res += ones[k] * (count - ones[k])
        return res

print Solution().totalHammingDistance([6, 1, 8, 6, 8])
'''
0 1 1 0
0 0 0 1
1 0 0 0
0 1 1 0
1 0 0 0
'''