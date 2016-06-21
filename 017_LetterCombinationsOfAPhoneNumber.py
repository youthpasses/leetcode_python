# coding:utf-8
# @sinner
# 16/6/18

'''
17. Letter Combinations of a Phone Number My Submissions QuestionEditorial Solution
Total Accepted: 84125 Total Submissions: 286891 Difficulty: Medium
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

d = {'0': ' ', '1': '*', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        res = list(d[digits[0]])
        for i in xrange(1, len(digits)):
            length = len(res)
            digit = digits[i]
            for x in xrange(0, length):
                for c in d[digit]:
                    res.append(res[x] + c)
            res = res[length:]
        return res

print Solution().letterCombinations('0210')
                