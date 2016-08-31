# coding:utf-8
# @sinner
# 16/8/31

'''
50. Pow(x, n)  QuestionEditorial Solution  My Submissions
Total Accepted: 105211
Total Submissions: 381840
Difficulty: Medium
Implement pow(x, n).
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n > 0:
            return self.power(x, n)
        else:
            return 1.0 / self.power(x, -n)

    def power(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        v = self.power(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x


print Solution().myPow(10, -2)

