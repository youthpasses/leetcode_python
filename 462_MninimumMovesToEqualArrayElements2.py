
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m = len(nums) / 2
        m = m - 1 if len(nums) % 2 == 0 else m
        x = nums[m]
        moves = 0
        for num in nums:
        	moves += abs(num - x)
        return moves
print Solution().minMoves2([203125577,-349566234,230332704,48321315,66379082,386516853,50986744,-250908656,-425653504,-212123143])