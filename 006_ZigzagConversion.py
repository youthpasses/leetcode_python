# coding:utf-8
# @sinner
# 16/6/5

'''
Total Accepted: 91005 Total Submissions: 374925 Difficulty: Easy
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
'''
用strDir保存每行的字符串
对于len(s)个字符，每 2 * numRows - 2 个字符一个循环，所以问题就转化为求编号与所在行数的对应关系问题
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        strDir = []
        for x in xrange(0, len(s)):
            # x1 = x / (2 * numRows - 2)
            x2 = x % (2 * numRows - 2)
            if x2 < numRows:
                if len(strDir) < numRows:
                    # 判断strDir是否保存了所有的numRows个字符串
                    strDir.append(s[x])
                else:
                    strDir[x2] += s[x]
            else:
                x3 = x2 % numRows
                strDir[x2 - (2 * x3 + 2)] += s[x]
        string = ''
        for x in xrange(0, numRows):
            string += strDir[x]
        return string

print Solution().convert('Abcde', 4)
