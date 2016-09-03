# coding:utf-8
# @sinner
# 16/9/2

'''
52. N-Queens II  QuestionEditorial Solution  My Submissions
Total Accepted: 49820
Total Submissions: 121260
Difficulty: Hard
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        res = []
        self.dp(res, [], 0, n)
        return len(res)

    def dp(self, res, s, level, n):
        if level == n:
            res.append(s)
        else:
            for y in xrange(0, n):
                if self.isValid(s, level, y):
                    self.dp(res, s + [y], level + 1, n)

    def isValid(self, s, x, y):
        for i in xrange(0, len(s)):
            j = s[i]
            if x == i or y == j:
                return False
            if abs(x - i) - abs(y - j) == 0 or x + y == i + j:
                return False
        return True

print Solution().totalNQueens(2)

