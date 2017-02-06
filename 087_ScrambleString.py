# coding:utf-8
# @makai
# 16/12/21

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        m, n  = len(s1), len(s2)
        if m != n or sorted(s1) != sorted(s2): return False
        if m < 4: return True
        for i in xrange(1, n):
        	if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        		return True
        	if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
        		return True
        return False

print Solution().isScramble("abab", "aabb")