# coding:utf-8
# @sinner
# 16/6/4

'''
Total Accepted: 154097 Total Submissions: 691539 Difficulty: Medium
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
'''
思路：
listc保存最长的字符串（无重复字符）
length保存记录到的最长的长度
对于s的每个字符char做如下判断：
    若char不在listc中，添加之，并判断listc的长度是否大于保存的length，若是，则更新length
    若char在listc中，将listc中保存的char及char之前的所有字符删除，然后存入新的char
循环结束，得到结果
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        listc = []
        length = 0
        for x in xrange(0, len(s)):
            char = s[x]
            if char not in listc:
                listc.append(char)
                if len(listc) > length:
                    length = len(listc)
            else:
                while listc[0] != char:
                    del listc[0]
                del listc[0]
                listc.append(char)
        return length

print Solution().lengthOfLongestSubstring('abcabcbb')
print Solution().lengthOfLongestSubstring('bbbbbbbb')
print Solution().lengthOfLongestSubstring('pwwkew')











