# coding:utf-8
# @sinner
# 16/8/31

'''
51. N-Queens  QuestionEditorial Solution  My Submissions
Total Accepted: 61233
Total Submissions: 223545
Difficulty: Hard
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.dp(res, [], 0, n)
        return res

    def dp(self, res, s, level, n):
        if level == n:
            ss = []
            for x in xrange(0, n):
                sss = ''
                for y in xrange(0, n):
                    if y == s[x]:
                        sss += 'Q'
                    else:
                        sss += '.'
                ss.append(sss)
            res.append(ss)
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

print Solution().solveNQueens(4)






