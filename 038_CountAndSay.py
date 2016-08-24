# coding:utf-8
# @sinner
# 16/8/21

'''
38. Count and Say  QuestionEditorial Solution  My Submissions
Total Accepted: 93448
Total Submissions: 305392
Difficulty: Easy
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = '1'
        while n > 1:
            nowC = s[0]
            result = ''
            count = 0
            for c in s:
                if c == nowC:
                    count += 1
                else:
                    result += str(count) + nowC
                    nowC = c
                    count = 1
            result += str(count) + nowC
            s = result
            n -= 1
        return s

print Solution().countAndSay(5)









