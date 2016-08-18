# coding:utf-8
# @sinner
# 16/6/5

'''
Total Accepted: 143373 Total Submissions: 605215 Difficulty: Easy
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        pos_x = abs(x)
        while pos_x:
            result = result * 10 + pos_x % 10
            pos_x /= 10
        if result >= 2147483647:
            return 0
        return result if x >= 0 else result * (-1)


print Solution().reverse(-123401)