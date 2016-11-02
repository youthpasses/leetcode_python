# coding:utf-8
# @sinner
# 16/9/27

'''
72. Edit Distance  QuestionEditorial Solution  My Submissions
Total Accepted: 68513
Total Submissions: 229060
Difficulty: Hard
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        res = [[0 for x in range(n + 1)] for y in range(m + 1)]
        for x in xrange(0, m + 1):
            res[x][0] = x
        for x in xrange(0, n + 1):
            res[0][x] = x
        for x in xrange(1, m + 1):
            for y in xrange(1, n + 1):
                res[x][y] = min(res[x - 1][y] + 1, res[x][y - 1] + 1)
                if word1[x - 1] != word2[y - 1]:
                    res[x][y] = min(res[x][y], res[x - 1][y - 1] + 1)
                else:
                    res[x][y] = min(res[x][y], res[x - 1][y - 1] + 0)
        return res[m][n]

print Solution().minDistance('intention', 'execution')














