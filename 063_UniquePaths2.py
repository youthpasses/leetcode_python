# coding:utf-8
# @sinner
# 16/9/11

'''
63. Unique Paths II  QuestionEditorial Solution  My Submissions
Total Accepted: 77387
Total Submissions: 255456
Difficulty: Medium
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        d = [[0 for x in xrange(m)] for y in xrange(n)]
        d[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in xrange(0, n):
            for j in xrange(0, m):
                if obstacleGrid[i][j] != 1:
                    if i > 0:
                        d[i][j] += d[i - 1][j]
                    if j > 0:
                        d[i][j] += d[i][j - 1]
        return d[n - 1][m - 1]


print Solution().uniquePathsWithObstacles([[0, 0]])





