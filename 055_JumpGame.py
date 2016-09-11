# coding:utf-8
# @sinner
# 16/9/4

'''
55. Jump Game  QuestionEditorial Solution  My Submissions
Total Accepted: 90638
Total Submissions: 313528
Difficulty: Medium
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for x in xrange(0, len(nums)):
            if x <= reach and reach < x + nums[x]:
                reach = x + nums[x]
        return reach >= len(nums) - 1

print Solution().canJump([3,2,1,0,4])

'''
动态规划，超时

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = []
        self.dp(reach, nums, 0)
        return True if len(reach) != 0 else False

    def dp(self, reach, nums, index):
        if index >= len(nums) - 1:
            reach.append(index)
        else:
            num = nums[index]
            if num >= 1:
                for x in xrange(1, num + 1):
                    self.dp(reach, nums, index + x)


print Solution().canJump([])
'''




