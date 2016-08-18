# coding:utf-8
# @sinner
# 16/6/7

'''
28. Implement strStr() My Submissions QuestionEditorial Solution
Total Accepted: 109978 Total Submissions: 436570 Difficulty: Easy
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question
'''

'''
too easy
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        count = len(needle)
        for x in xrange(0, len(haystack) - count + 1):
            if haystack[x:x+count] == needle:
                return x
        return -1