# coding:utf-8
# @sinner
# 16/6/18

'''
16. 3Sum Closest My Submissions QuestionEditorial Solution
Total Accepted: 81330 Total Submissions: 276139 Difficulty: Medium
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums = tuple(nums)
        s = nums[0] + nums[1] + nums[2]
        saved_s = s
        dis = abs(s - target)
        for x in xrange(0, len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            num1 = nums[x]
            left = x + 1
            right = len(nums) - 1
            while left < right:
                s = num1 + nums[left] + nums[right]
                if s - target == 0:
                    return s
                elif s - target < 0:
                    left += 1
                else:
                    right -= 1
                now_dis = abs(s - target)
                if now_dis < dis:
                    dis = now_dis
                    saved_s = s
        return saved_s


print Solution().threeSumClosest([1, -2, 1, -4], 1)

