# coding:utf-8
# @makai
# 16/12/25

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if s[0] == '0': return 0
        if len(s) == 1: return 1
        res = [0 for x in xrange(len(s))]
        res[-1] = 0 if s[-1] == '0' else 1
        if s[-2] == '0': res[-2] = 0
        else: res[-2] = res[-1] + 1 if int(s[-2:]) <= 26 else res[-1]
        for x in xrange(3, len(s) + 1):
        	if s[-x] == '0': res[-x] = 0
        	else: res[-x] = res[-(x-1)] + res[-(x-2)] if int(s[-x:-(x-2)]) <= 26 else res[-(x-1)]
        return res[0]

print Solution().numDecodings('1011')
