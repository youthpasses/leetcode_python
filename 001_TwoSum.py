# coding:utf-8
# @sinner
# 16/6/4

'''
Total Accepted: 239594 Total Submissions: 1001231 Difficulty: Easy
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
思路：
x: 0 -> len(nums) - 1, y: x + 1 -> len(nums)，遍历一遍，找到相加等于target即停止并返回x, y
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # index1 = 0
        # index2 = 0
        count = len(nums)
        for x in xrange(0, count - 1):
            for y in xrange(x + 1, count):
                print x, y
                if (nums[x] + nums[y]) == target:
                    return [x, y]

solu = Solution()
print solu.twoSum([2, 4, 9, 0, 1], 5)
