# coding: utf-8
# @makai
# 16/11/6

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        haveDic = {}
        counter = 0
        for c in t:
            if c not in dic.keys():
                dic[c] = 1
                haveDic[c] = 0
            else:
                dic[c] += 1
        l = 0
        r = 0
        minL = 0
        minLen = len(s) + 1
        while r < len(s):
            if s[r] in haveDic.keys():
                haveDic[s[r]] += 1
                if haveDic[s[r]] <= dic[s[r]]:
                    counter += 1
            r += 1
            while counter == len(t):
                if r - l < minLen:
                    minL = l
                    minLen = r - l
                c = s[l]
                if c in haveDic.keys():
                    haveDic[c] -= 1
                    if haveDic[c] < dic[c]:
                        counter -= 1
                l += 1
        return s[minL : minL + minLen] if minLen < len(s) + 1 else ''

print Solution().minWindow('ACBANC', 'BN')