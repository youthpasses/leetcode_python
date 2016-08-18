# coding:utf-8
# @sinner
# 16/6/21

'''
29. Divide Two Integers My Submissions QuestionEditorial Solution
Total Accepted: 69950 Total Submissions: 443435 Difficulty: Medium
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

Subscribe to see which companies asked this question
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        if divisor == 0:
            return -1
        positive = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if abs(divisor) == 1:
            res = dividend * positive
            res = min(2147483647, res) if res > 0 else res
            return res
        s1 = str(dividend)
        s2 = str(divisor)
        num = int(s1[:len(s2)])
        res = 0
        for x in xrange(len(s1) - len(s2) + 1):
            i = 0
            while num >= 0:
                num -= divisor
                i += 1
            res = 10 * res + (i - 1)
            left = num + divisor
            if x != len(s1) - len(s2):
                num = int(s1[len(s2) + x:len(s2) + x + 1])
                num += left * 10
        return positive * res

print Solution().divide(23, -6)

