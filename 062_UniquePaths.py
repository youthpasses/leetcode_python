# coding:utf-8
# @sinner
# 16/9/7

'''
62. Unique Paths  QuestionEditorial Solution  My Submissions
Total Accepted: 102268
Total Submissions: 270318
Difficulty: Medium
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[0 for x in xrange(m)] for y in xrange(n)]
        d[0][0] = 1
        for i in xrange(0, n):
            for j in xrange(0, m):
                if i > 0:
                    d[i][j] += d[i - 1][j]
                if j > 0:
                    d[i][j] += d[i][j - 1]
        return d[n - 1][m - 1]

print Solution().uniquePaths(100, 100)

'''
# Time Limit Exceeded

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = []
        self.bt(0, 0, m, n, res)
        return len(res)

    def bt(self, x, y, m, n, res):
        if x == m - 1 and y == n - 1:
            res.append(1)
        else:
            if x < m - 1:
                self.bt(x + 1, y, m, n, res)
            if y < n - 1:
                self.bt(x, y + 1, m, n, res)


print Solution().uniquePaths(100, 100)
'''






