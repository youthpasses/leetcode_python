# coding:utf-8
# @sinner
# 16/8/31

'''
49. Group Anagrams  QuestionEditorial Solution  My Submissions
Total Accepted: 88566
Total Submissions: 300315
Difficulty: Medium
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorts = {}
        res = []
        temp = ''
        for s in strs:
            temp = ''.join(sorted(list(s[:])))
            if not sorts.has_key(temp):
                sorts[temp] = len(sorts)
                res.append([s])
            else:
                res[sorts[temp]].append(s)
        return res


print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])









