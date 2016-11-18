# coding:utf-8
# @sinner
# 16/11/12

'''
84. Largest Rectangle in Histogram   QuestionEditorial Solution  My Submissions
Total Accepted: 74768
Total Submissions: 294616
Difficulty: Hard
Contributors: Admin
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        s = 0
        for i in xrange(1, len(heights)):
        	while heights[i] < heights[stack[-1]]:
        		idx = stack.pop()
        		s = max(s, heights[idx] * (i - stack[-1] - 1))
        	stack.append(i)
        return s

print Solution().largestRectangleArea([2,1,2])