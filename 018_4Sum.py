# coding:utf-8
# @sinner
# 16/6/18

'''
18. 4Sum My Submissions QuestionEditorial Solution
Total Accepted: 76142 Total Submissions: 315377 Difficulty: Medium
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        nums = tuple(nums)
        rightmost = len(nums) - 1
        for x in xrange(0, len(nums) - 3):
            num0 = nums[x]
            target_now = target - num0
            for i in xrange(x + 1, len(nums) - 2):
                left = i + 1
                right = rightmost
                num1 = nums[i]
                while left < right:
                    num2 = nums[left]
                    num3 = nums[right]
                    if num2 + num3 + num1 == target_now:
                        res = [num0, num1, num2, num3]
                        res.sort()
                        if res not in results:
                            results.append(res)
                        left += 1
                        right -= 1
                    elif num1 + num2 + num3 > target_now:
                        right -= 1
                    else:
                        left += 1
        return results

print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
