# coding:utf-8
# @sinner
# 16/8/23

'''
42. Trapping Rain Water  QuestionEditorial Solution  My Submissions
Total Accepted: 76419
Total Submissions: 228220
Difficulty: Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        leftmax, rightmax = 0, 0
        res = 0
        while left <= right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if leftmax < rightmax:
                res += leftmax - height[left]
                left += 1
            else:
                res += rightmax - height[right]
                right -= 1
        return res


print Solution().trap([])



