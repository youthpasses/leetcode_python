# coding:utf-8
# @makai
# 16.12.20

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        f = {x:False for x in xrange(len(s) + 1)}
        f[0] = True
        for i in xrange(1, len(s) + 1):
        	for j in xrange(0, i):
        		if f[j] and s[j:i] in wordDict:
        			f[i] = True
        return f[len(s)]

print Solution().wordBreak("leetcode", ["leetcode"])