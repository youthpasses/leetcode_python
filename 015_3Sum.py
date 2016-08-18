# coding:utf-8
# @sinner
# 16/6/17

'''
15. 3Sum My Submissions QuestionEditorial Solution
Total Accepted: 123397 Total Submissions: 644840 Difficulty: Medium
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nd={}
        for n in nums:
            nd[n]=nd.get(n,0)+1
        sol=[]
        for i in nd:
            nd[i]-=1
            for j in nd:
                if nd[j]<=0:
                    continue
                nd[j]-=1
                r=0-i-j
                if nd.get(r,0)>0:
                    sol.append(sorted([i,j,r]))
                nd[j]+=1
        sol=list(set(map(tuple,sol)))
        sol.sort()
        return sol
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        nums = tuple(nums)
        rightmost = len(nums) - 1
        for i in xrange(0, len(nums) - 2):
            left = i + 1
            right = rightmost
            num1 = nums[i]
            while left < right:
                num2 = nums[left]
                num3 = nums[right]
                if num2 + num3 == -num1:
                    res = [num1, num2, num3]
                    if res not in results:
                        results.append(res)
                    left += 1
                    right -= 1
                elif num2 + num3 > -num1:
                    right -= 1
                else:
                    left += 1
        return results

print Solution().threeSum([-1, 1, 2, -4, 0, -1])