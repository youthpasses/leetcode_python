# coding:utf-8
# @sinner
# 16/6/19

'''
22. Generate Parentheses My Submissions QuestionEditorial Solution
Total Accepted: 92583 Total Submissions: 244788 Difficulty: Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        l = []
        res = []
        self.a(res, l, n)
        return res

    def a(self, res, l, n):
        if len(l) == 2 * n:
            l = ''.join(l)
            res.append(l)
            return
        if self.leftValid(l, n):
            l.append('(')
            self.a(res, l, n)
            l.pop()

        if self.rightValid(l):
            l.append(')')
            self.a(res, l, n)
            l.pop()

    def leftValid(self, l, n):
        left_count = l.count('(')
        if left_count == n:
            return False
        return True

    def rightValid(self, l):
        left_count = l.count('(')
        right_count = l.count(')')
        if left_count > right_count:
            return True
        return False
        

print Solution().generateParenthesis(3)