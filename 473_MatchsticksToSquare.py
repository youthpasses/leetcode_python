# coding:utf-8
# @makai
# 16/12/18


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4: return False
        totalLength = sum(nums)
        if totalLength % 4: return False
        length = totalLength / 4
        if max(nums) > length: return False
        target = [length] * 4
        nums.sort(reverse=True)
        return self.dfs(nums, 0, target)
    
    def dfs(self, nums, pos, target):
        if pos == len(nums): return True
        for i in range(4):
            if target[i] >= nums[pos]:
                target[i] -= nums[pos]
                if self.dfs(nums, pos+1, target): return True
                target[i] += nums[pos]
        return False

print Solution().makesquare([3,1,3,3,10,7,10,3,6,9,10,3,7,6,7])


'''
    if len(nums) < 4: return False
    totalLength = sum(nums)
    if totalLength % 4: return False
    length = totalLength / 4
    if max(nums) > length: return False
    target = [length] * 4
    return self.dfs(nums, 0, target)
    # return self.dp(0, nums, length, 0)
def dp(self, count, nums, length, nowL):
    if count == 3: return True
    if nowL == length:
        if self.dp(count + 1, nums, length, 0): return True
    for i, num in enumerate(nums):
        if nowL + num <= length:
            del nums[i]
            if self.dp(count, nums, length, nowL + num): return True
            nums.insert(i, num)
    return False
'''