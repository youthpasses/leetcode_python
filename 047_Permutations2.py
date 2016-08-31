# coding:utf-8
# @sinner
# 16/8/26

'''
47. Permutations II  QuestionEditorial Solution  My Submissions
Total Accepted: 83078
Total Submissions: 282992
Difficulty: Medium
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ret = [[]]
        for n in nums:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    if i < l and seq[i] == n:
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret

print Solution().permuteUnique([1, 2, 1, 2])


'''
//超时

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = [nums[:]]
        que = [nums[:]]
        count = 1
        for x in xrange(1, len(nums) + 1):
            count = count * x
        while len(res) < count and que:
            a = que.pop()
            for x in xrange(0, len(a) - 1):
                for y in xrange(1, len(a)):
                    if a[x] != a[y]:
                        t = a[x]
                        a[x] = a[y]
                        a[y] = t
                        if a not in res:
                            res.append(a[:])
                            que.insert(0, a[:])
                        t = a[x]
                        a[x] = a[y]
                        a[y] = t
        return res

print Solution().permuteUnique([1, 1, 2, 2])
'''


'''
//回溯法，超时

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        self.bt(nums, [], res)
        return res

    def bt(self, nums, p, res):
        if not nums and p not in res:
            res.append(p)
        else:
            for i, n in enumerate(nums):
                nums.pop(i)
                self.bt(nums, p + [n], res)
                nums.insert(i, n)


print Solution().permuteUnique([1, 1, 0, 0, 1, -1, -1, 1])
'''