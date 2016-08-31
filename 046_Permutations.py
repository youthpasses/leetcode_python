# coding:utf-8
# @sinner
# 16/8/26

'''
46. Permutations  QuestionEditorial Solution  My Submissions
Total Accepted: 115342
Total Submissions: 305191
Difficulty: Medium
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        self.bt(nums, res, 0)
        return res

    def bt(self, nums, res, level):
        if nums not in res:
            res.append(nums)
        if level == len(nums) - 1:
            return
        else:
            for i in xrange(level, len(nums)):
                a = nums[:]
                t = a[level]
                a[level] = a[i]
                a[i] = t
                self.bt(a, res, level + 1)

print Solution().permute([1, 2, 3])


'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        self.bt(nums, [], res, 0)
        return res

    def bt(self, nums, p, res, count):
        if count == len(nums):
            if p not in res:
                res.append(p)
        else:
            for x in nums:
                if x not in p:
                    self.bt(nums, p + [x], res, count + 1)

print Solution().permute([2])
'''







