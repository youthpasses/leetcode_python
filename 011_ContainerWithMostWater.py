# coding:utf-8
# @sinner
# 16/6/16


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = min(height[left], height[right]) * (right - left)
        while right > left:
            print left, right, min(height[left], height[right]) * (right - left)
            l = height[left]
            r = height[right]
            if l > r:
                while right > left and height[right] <= r:
                    right -= 1
            else:
                while left < right and height[left] <= l:
                    left += 1
            if left < right:
                area = max(area, min(height[left], height[right]) * (right - left))
        return area
                    
print Solution().maxArea([1, 1])