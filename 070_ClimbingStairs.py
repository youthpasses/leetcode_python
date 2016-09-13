# coding:utf-8
# @sinner
# 16/9/13

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        d = {}
        d[1] = 1
        d[2] = 2
        for x in xrange(3, n + 1):
            d[x] = d[x - 2] + d[x - 1]
        return d[n]

print Solution().climbStairs(10)