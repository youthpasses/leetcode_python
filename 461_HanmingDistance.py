# coding:utf-8
# @makai
# 16/12/18


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        '''
        a = bin(x)[2:]
        b = bin(y)[2:]
        length = min(len(a), len(b))
        res = 0
        for x in xrange(1, length + 1):
            if a[-x] != b[-x]:
                res += 1
        c = a if len(b) == length else b
        for x in xrange(length + 1, len(c) + 1):
            if c[-x] == '1':
                res += 1
        return res
		'''
		res = 0
        while x or y:
            res += (x % 2) ^ (y % 2)
            x /= 2
            y /= 2
        return res
print Solution().hammingDistance(1349232, 4423423553)