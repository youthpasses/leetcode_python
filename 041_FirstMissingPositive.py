# coding:utf-8
# @sinner
# 16/8/23

'''
41. First Missing Positive  QuestionEditorial Solution  My Submissions
Total Accepted: 72315
Total Submissions: 296875
Difficulty: Hard
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0] * (len(nums) + 1)
        for n in [x for x in nums if x > 0 and x < len(l)]:
            l[n] = 1
        for x in xrange(1, len(l)):
            if l[x] == 0:
                return x
        return len(l)


print Solution().firstMissingPositive([3, 4, -1, 1])