# coding:utf-8
# @sinner
# 16/9/11

'''
64. Minimum Path Sum  QuestionEditorial Solution  My Submissions
Total Accepted: 83804
Total Submissions: 230929
Difficulty: Medium
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        d = [[0 for x in xrange(n)] for y in xrange(m)]
        for i in xrange(0, m):
            for j in xrange(0, n):
                if i > 0 and j > 0:
                    d[i][j] = min(grid[i][j] + d[i - 1][j], grid[i][j] + d[i][j - 1])
                elif i > 0 and j == 0:
                    d[i][j] = grid[i][j] + d[i - 1][j]
                elif i == 0 and j > 0:
                    d[i][j] = grid[i][j] + d[i][j - 1]
                else:
                    d[i][j] = grid[i][j]
        return d[m - 1][n - 1]




