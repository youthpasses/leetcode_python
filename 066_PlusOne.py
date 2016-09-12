# coding:utf-8
# @sinner
# 16/9/12

'''
66. Plus One  QuestionEditorial Solution  My Submissions
Total Accepted: 121998
Total Submissions: 342645
Difficulty: Easy
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Subscribe to see which companies asked this question
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        jinwei = False
        for x in xrange(len(digits) - 1, -1, -1):
            print x
            if digits[x] != 9:
                digits[x] += 1
                jinwei = False
                break
            else:
                digits[x] = 0
                jinwei = True
        if jinwei:
            digits.insert(0, 1)
        return digits

print Solution().plusOne([8, 9, 9])