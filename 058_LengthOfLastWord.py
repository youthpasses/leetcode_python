# coding:utf-8
# @sinner
# 16/9/6

'''
58. Length of Last Word  QuestionEditorial Solution  My Submissions
Total Accepted: 108455
Total Submissions: 357271
Difficulty: Easy
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().split(' ')
        if len(s) == 0:
            return 0
        else:
            return len(s[-1])

print Solution().lengthOfLastWord('a  ')