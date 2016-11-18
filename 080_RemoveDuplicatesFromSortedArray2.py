# coding:utf-8
# @sinner
# 16/11/10

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        count = 0
        for num in nums:
        	if num not in dic.keys():
        		dic[num] = 1
        		nums[count] = num
        		count += 1
        	else:
        		if dic[num] == 1:
        			nums[count] = num
        			dic[num] = 2
        			count += 1
        nums = nums[:count]
        return count

print Solution().removeDuplicates([1,1,1,2,2,2,3,3,4,5,5,5,6,7,8,8,9,9,9])