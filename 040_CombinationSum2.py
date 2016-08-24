# coding:utf-8
# @sinner
# 16/8/23

'''
40. Combination Sum II  QuestionEditorial Solution  My Submissions
Total Accepted: 79486
Total Submissions: 272569
Difficulty: Medium
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.bt(result, [], candidates, target, 0)
        return result

    def bt(self, result, l, candidates, target, level):
        if target == 0:
            # l.sort()
            # if l not in result:
            result.append(l)
        else:
            for x in xrange(level, len(candidates)):
                num = candidates[x]
                if num <= target:
                    self.bt(result, l + [num], candidates, target - num, x + 1)

print Solution().combinationSum2([1, 2], 4)







