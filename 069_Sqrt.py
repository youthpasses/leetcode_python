# coding:utf-8
# @sinner
# 169/13

'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return x
        l = 0
        r = x
        while l < r - 1:
            m = (l + r) / 2
            if m * m <= x:
                l = m
            else:
                r = m
        return l
print Solution().mySqrt(9)