# coding:utf-8
# @sinner
# 16/6/4

'''
Total Accepted: 96912 Total Submissions: 513637 Difficulty: Hard
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''
'''
使用Python内置函数extend进行nums1和nums2的合并，然后用sort函数进行排序
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 0:
            return float(nums1[length / 2 - 1] + nums1[length / 2]) / 2
        else:
            return nums1[length / 2]


print Solution().findMedianSortedArrays([1, 2, 5, 7, 9], [2, 4, 7, 8, 9])