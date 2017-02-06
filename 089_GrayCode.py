# coding:utf-8
# @makai
# 16/12/21

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results
        '''
        res = [0]
        self.bt(res, n)
        return res

    def bt(self, res, n):
    	if len(res) == 2 ** n: return
    	for i in xrange(1, 2 ** n):
    		if self.f(n, res[-1] ^ i) and i not in res:
    			res.append(i)
    			self.bt(res, n)
    			break

    def f(self, n, m):
    	x = 0
    	while x < n:
    		if 2 ** x == m: return True
    		x += 1
    	return False
	'''
print Solution().grayCode(2)