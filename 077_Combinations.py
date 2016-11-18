# coding:utf-8
# @makai
# 16/11/6

class Solution(object):
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        kk = min(k, n - k)
        self.hehe(res, n, kk, 0, [])
        if kk != k:
            nums = xrange(1, n + 1)
            res = [list(set(x) ^ set(nums)) for x in res]
        return res

    def hehe(self, res, n, kk, i, l):
        if kk == 0:
            res.append(l)
            return
        for j in xrange(i + 1, n + 1):
            self.hehe(res, n, kk - 1, j, l + [j])

print Solution().combine(5, 3)