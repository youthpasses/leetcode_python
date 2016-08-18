# coding:utf-8
# @sinner
# 16/8/17

'''
32. Longest Valid Parentheses  QuestionEditorial Solution  My Submissions
Total Accepted: 70086
Total Submissions: 307903
Difficulty: Hard
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Subscribe to see which companies asked this question
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        dp = []
        for x in xrange(0, len(s)):
            dp.append(0)
        for i in xrange(1, len(s)):
            if s[i] == ')':
                begin = i - 1 - dp[i - 1]
                if begin > -1:
                    if s[begin] == '(':
                        dp[i] = + dp[i - 1] + 2
                        if begin - 1 >= 0:
                            dp[i] += dp[begin - 1]
        return max(dp)

print Solution().longestValidParentheses("()()))))()()(")