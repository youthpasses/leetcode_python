# coding:utf-8
# @sinner
# 16/9/17

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstRaw = False
        firstCol = False
        for x in xrange(0, m):
            if matrix[x][0] == 0:
                firstCol = True
                break
        for x in xrange(0, n):
            if matrix[0][x] == 0:
                firstRaw = True
                break
        for x in xrange(0, m):
            for y in xrange(0, n):
                if matrix[x][y] == 0:
                    if x != 0:
                        matrix[x][0] = 0
                    if y != 0:
                        matrix[0][y] = 0
        for x in xrange(1, n):
            if matrix[0][x] == 0:
                for y in xrange(0, m):
                    matrix[y][x] = 0
        for x in xrange(0, m):
            if matrix[x][0] == 0:
                for y in xrange(0, n):
                    matrix[x][y] = 0
        if firstRaw:
            for x in xrange(0, n):
                matrix[0][x] = 0
        if firstCol:
            for x in xrange(0, m):
                matrix[x][0] = 0
        print matrix

Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
