#
# coding:utf-8
# @makai
# 17/1/8
#
############################

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = list(''.join(S.split('-')))
        for i, c in enumerate(s):
        	if ord(c) >=97: s[i] = chr(ord(c) - 32)
        n = len(s) / K if len(s) % K == 0 else len(s) / K + 1
        p = [''.join(s[-K:])]
        for i in xrange(2, n + 1):
        	start = -i * K
        	end = start + K
        	p.insert(0, ''.join(s[start:end]))
        return '-'.join(p)

print Solution().licenseKeyFormatting("24kd-fda-e", 6)