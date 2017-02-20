# coding:utf-8
# @makai
# 17/2/20

class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        sums = {-1:0}
        s = 0
        for i, x in enumerate(machines):
        	s += x
        	sums[i] = s
        if s % len(machines) != 0: return -1
        length = len(machines)
        ave = s / length
        res = []
        for i, x in enumerate(machines):
        	lsum = sums[i-1]
        	rsum = s - lsum - x
        	L = ave * i - lsum
        	R = ave * (length - i - 1) - rsum
        	if L > 0 and R > 0: res.append(L + R)
        	else: res.append(max(abs(L), abs(R)))
        return max(res)

print Solution().findMinMoves([3, 0, 3])