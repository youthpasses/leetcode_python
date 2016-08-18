# coding:utf-8
# @sinner
# 16/6/21

'''
30. Substring with Concatenation of All Words My Submissions QuestionEditorial Solution
Total Accepted: 57037 Total Submissions: 270541 Difficulty: Hard
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

'''
截取所有words长的substring，在isValid函数里判断是否与所有的words匹配
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        length = len(words[0])
        if length > len(s):
            return []
        count_c = len(words) * length
        res = []
        i = 0
        while i < len(s) - count_c + 1:
            word = s[i:i + length]
            if word in words:
                ss = s[i:i + count_c]
                if self.isValid(ss, words, length):
                    res.append(i)
                i += 1
            else:
                i += 1
        return res

    def isValid(self, ss, words, length):
        words_ss = []
        print ss
        for x in xrange(len(ss) / length):
            word = ss[x * length:(x + 1) * length]
            words_ss.append(word)
        for word in words:
            if word in words_ss:
                words_ss.remove(word)
            else:
                return False
        return True

print Solution().findSubstring('aaaaaaaa', ["aa", "aa", "aa"])


