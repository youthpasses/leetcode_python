# coding:utf-8
# @sinner
# 16/8/23

'''
39. Combination Sum  QuestionEditorial Solution  My Submissions
Total Accepted: 107339
Total Submissions: 325591
Difficulty: Medium
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.bt(result, [], candidates, target)
        return result

    def bt(self, result, l, candidates, target):
        if target == 0:
            result.append(l)
        else:
            for num in [x for x in candidates if x <= target and ((len(l) > 0 and x >= l[-1]) or len(l) == 0)]:
                self.bt(result, l + [num], candidates, target - num)
            

print Solution().combinationSum([2, 3, 6, 7], 7)






