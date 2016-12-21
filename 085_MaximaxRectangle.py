# coding:utf-8
# @sinner
# 16/11/20

'''
85. Maximal Rectangle   QuestionEditorial Solution  My Submissions
Total Accepted: 53926
Total Submissions: 211190
Difficulty: Hard
Contributors: Admin
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
        	return 0
        n = len(matrix[0])
        heights = [0] * (n + 2)
        res = 0
        for row in matrix:
        	for x in xrange(n):
        		heights[x + 1] = heights[x + 1] + 1 if row[x] == '1' else 0
        	stack = [0]
        	for i in xrange(1, len(heights)):
    			while heights[i] < heights[stack[-1]]:
    				idx = stack.pop()
    				res = max(res, heights[idx] * (i - stack[-1] - 1))
    			stack.append(i)
        return res

print Solution().maximalRectangle(["10100","10111","11111","10010"])