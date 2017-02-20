# coding:utf-8
# @makai
# 17/2/19

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = []
        self.bt(res, [], 1, N)
        return len(res)

    def bt(self, res, now, i, N):
    	if i == N+1:
    		res.append(now)
    	else:
    		for j in xrange(1, N+1):
    			if j not in now and (j%i == 0 or i%j == 0):
    				self.bt(res, now + [j], i + 1, N)
print Solution().countArrangement(15)