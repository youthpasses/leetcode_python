# coding:utf-8
# @sinner
# 16/6/22

'''
31. Next Permutation My Submissions QuestionEditorial Solution
Total Accepted: 69552 Total Submissions: 258518 Difficulty: Medium
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

'''
思路：从后往前遍历，找到第一对i,j，使得nums[i] < nums[j]，然后找到j即j之后的稍大于nums[i]的元素与nums[i]交换，然后对i之后的元素排序
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        if i == -1:
            return
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i != 0:
            j = i
            i = i - 1
            lastSmall = nums[j]
            lastSmall_index = j
            for x in xrange(j, len(nums)):
                if nums[x] > nums[i] and nums[x] <= lastSmall:
                    lastSmall = nums[x]
                    lastSmall_index = x
            nums[lastSmall_index] = nums[i]
            nums[i] = lastSmall
            left = j
            right = len(nums) - 1
            while left < right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1
        else:
            nums.sort()
Solution().nextPermutation([2, 3, 1, 3, 3])



# for x in xrange(j, len(nums) - 1):
#                 for y in xrange(j, len(nums) - (x - j)):
#                     print x, y







