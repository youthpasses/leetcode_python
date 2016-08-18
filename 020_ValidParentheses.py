# coding:utf-8
# @sinner
# 16/6/6

'''
Total Accepted: 111901 Total Submissions: 376108 Difficulty: Easy
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        savedC = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                savedC.append(c)
            else:
                if len(savedC) == 0:
                    return False
                if (c == ')' and savedC.pop() != '(') or (c == '}' and savedC.pop() != '{') or (c == ']' and savedC.pop() != '['):
                    return False
        return not savedC

print Solution().isValid('[]')
