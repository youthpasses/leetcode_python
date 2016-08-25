# coding:utf-8
# @sinner
# 16/8/25

'''
45. Jump Game II  QuestionEditorial Solution  My Submissions
Total Accepted: 71196
Total Submissions: 277041
Difficulty: Hard
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''


# 贪心算法
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        start = 0
        maxDis = nums[0]
        end = 0 + nums[0]
        step = 1
        while end < len(nums) - 1:
            for x in xrange(start + 1, end + 1):
                maxDis = max(maxDis, nums[x] + x)
            start = end
            end = maxDis
            step += 1
        return step

print Solution().jump([5, 6, 5, 3])

# 动态规划算法，超时
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        res = []
        self.dp(nums, 0, 0, res)
        return 0 if not res else min(res)

    def dp(self, nums, index, step, res):
        if index != len(nums) - 1 and nums[index] == 0:
            return
        if nums[index] + index >= len(nums) - 1:
            if index == 0 or index != len(nums) - 1:
                step += 1
            res.append(step)
        else:
            for x in xrange(1, nums[index] + 1):
                self.dp(nums, index + x, step + 1, res)

print Solution().jump([5,6,5,3,9,8,3,1,2,8,2,4,8,3,9,1,0,9,4,6,5,9,8,7,4,2,1,0,2])
'''








