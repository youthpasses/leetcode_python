# coding:utf-8
# @sinner
# 16/8/30

'''
48. Rotate Image  QuestionEditorial Solution  My Submissions
Total Accepted: 78089
Total Submissions: 217538
Difficulty: Medium
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

'''
思路：一层一层的转
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in xrange(0, n / 2):
            for i in xrange(layer, n - layer - 1):
                temp = matrix[i][layer]
                matrix[i][layer] = matrix[n - 1 - layer][i]
                matrix[n - 1 - layer][i] = matrix[n - 1 - i][n - 1 - layer]
                matrix[n - 1 - i][n - 1 - layer] = matrix[layer][n - 1 - i]
                matrix[layer][n - 1 - i] = temp


Solution().rotate([[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]])








