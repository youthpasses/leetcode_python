# coding:utf-8
# @sinner
# 16/6/6

'''
Total Accepted: 88041 Total Submissions: 220139 Difficulty: Easy
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
'''
思路：
应当注意，对于每个V X L C D M，他们的左边最多有一个比他小的数是跟它组合的
'''

d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        result, p = 0, 'M'  # M为最大
        for c in s:
            result, p = result + d[c] if d[c] <= d[p] else result + d[c] - 2 * d[p], c
        return result

print Solution().romanToInt('MMMCMXCIX')
