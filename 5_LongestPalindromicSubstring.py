# coding:utf-8
# @sinner
# 16/6/4

'''
Total Accepted: 111904 Total Submissions: 480084 Difficulty: Medium
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''
'''
思路：
large保存最长的长度
subStr保存最长的回文子字符串
遍历一遍s的所有字符s[x]
    1、若s[x] = s[x - 1]，说明两个相同的字符挨着，然后一个索引pre向前，一个索引nex向后遍历，结束条件是：越界和s[pre] != s[nex]
    2、若s[x + 1] = s[x - 1]，说明在字符s[x]左右的两个字符相同，然后一个索引pre向前，一个索引nex向后遍历，结束条件是：越界和s[pre] != s[nex]
    需要注意的是，'aaa'，'aaaa'这样的字符串，1、2条件均满足，所以需要进行两次遍历，取最长的。
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        large = 0
        subStr = ''
        if s[0] == s[1]:
            large = 2
            subStr = s[0:2]
        for x in xrange(1, len(s) - 1):
            if s[x + 1] == s[x]:
                # 'aaaa'
                pre = x - 1
                nex = x + 2
                while (pre >= 0) and (nex < len(s)) and (s[pre] == s[nex]):
                    pre -= 1
                    nex += 1
                pre += 1
                nex -= 1
                length_sub = nex - pre + 1
                if length_sub > large:
                    large = length_sub
                    subStr = s[pre:nex + 1]

            if s[x + 1] == s[x - 1]:
                # 'aaa'
                pre = x - 1
                nex = x + 1
                while (pre >= 0) and (nex < len(s)) and (s[pre] == s[nex]):
                    pre -= 1
                    nex += 1
                pre += 1
                nex -= 1
                length_sub = nex - pre + 1
                if length_sub > large:
                    large = length_sub
                    subStr = s[pre:nex + 1]
        return subStr


print Solution().longestPalindrome('ccd')






                