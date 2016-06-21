# coding:utf-8
# @sinner
# 16/6/8

'''
349. Intersection of Two Arrays My Submissions QuestionEditorial Solution
Total Accepted: 15369 Total Submissions: 34225 Difficulty: Easy
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

'''
too easy
'''


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        for x in nums1:
            if x in nums2:
                res.append(x)
        return res

        '''
        # one line
        return list(set(nums1) & set(nums2))
        '''

print Solution().intersection([1,2,3], [3,2,1,4,8])