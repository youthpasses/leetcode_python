# coding:utf-8
# @sinner
# 16/9/17

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        while x < m:
            if matrix[x][0] > target:
                x -= 1
                break
            x += 1
        if x == m:
            x -= 1
        left = 0
        right = n - 1
        y = (left + right) / 2
        while left < right:
            if matrix[x][y] > target:
                right = y - 1
                y = (left + right) / 2
            elif matrix[x][y] < target:
                left = y + 1
                y = (left + right) / 2
            else:
                break
        return True if matrix[x][y] == target else False


print Solution().searchMatrix([[1],   [3],  [5],  [7]], 7)








