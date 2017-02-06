# coding:utf-8
# @makai
# 16/12/27

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0 for x in xrange(n + 1)]
        G[0] = 1
        G[1] = 1
        for i in xrange(2, n + 1):
        	for j in xrange(0, i):
        		G[i] += G[j] * G[i-j-1]
        return G[n]
print Solution().numTrees(2)