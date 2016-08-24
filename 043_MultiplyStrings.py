# coding:utf-8
# @sinner
# 16/8/24

'''
43. Multiply Strings  QuestionEditorial Solution  My Submissions
Total Accepted: 70996
Total Submissions: 288439
Difficulty: Medium
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        for y in xrange(0, len(num1)):
            n1 = ord(num1[len(num1) - y - 1]) - 48
            s = 0
            carry = 0
            for x in xrange(0, len(num2)):
                n2 = ord(num2[len(num2) - x - 1]) - 48
                a = n1 * n2 + carry
                if x != len(num2) - 1:
                    s += (a % 10) * (10 ** x)
                    carry = a / 10
                else:
                    s += a * (10 ** x)
            res += s * (10 ** y)
        return str(res)

print Solution().multiply('10', '789')










