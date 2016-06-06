# coding:utf-8
# @sinner
# 16/6/6

'''
Total Accepted: 103536 Total Submissions: 362795 Difficulty: Easy
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = ''
        noStop = True
        i = 0
        while noStop:
            char = ''
            if len(strs[0]) >= i + 1:
                char = strs[0][i]
            else:
                noStop = False
            for string in strs:
                if len(string) == i or string[i] != char:
                    noStop = False
            if noStop:
                res += char
            i += 1
        return res

print Solution().longestCommonPrefix([''])