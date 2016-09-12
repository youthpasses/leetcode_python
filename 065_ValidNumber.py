# coding:utf-8
# @sinner
# 16/9/12

'''
65. Valid Number  QuestionEditorial Solution  My Submissions
Total Accepted: 52995
Total Submissions: 426504
Difficulty: Hard
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
'''


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = [[-1, 0,  1,  2, -1, 3],
            [-1, -1, -1,  2, -1, 3],
            [-1, -1, -1, -1, -1, 4],
            [-1,  5, -1,  4,  6, 3],
            [-1,  5, -1, -1,  6, 4],
            [-1,  5, -1, -1, -1, -1],
            [-1, -1,  7, -1, -1, 8],
            [-1, -1, -1, -1, -1, 8],
            [-1,  5, -1, -1, -1, 8]]
        state = 0
        for c in s:
            if state == -1:
                break
            else:
                if c == ' ':
                    state = t[state][1]
                elif c == '+' or c == '-':
                    state = t[state][2]
                elif c == '.':
                    state = t[state][3]
                elif c == 'e' or c == 'E':
                    state = t[state][4]
                elif ord(c) >= 48 and ord(c) <= 57:
                    state = t[state][5]
                else:
                    state = t[state][0]
        return state == 3 or state == 4 or state == 5 or state == 8






