# coding:utf-8
# @sinner
# 16/6/5

'''
Total Accepted: 104965 Total Submissions: 774762 Difficulty: Easy
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
去掉前面的空格字符
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
数字后面可能包含其他字符，要忽略之
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
如果str中第一个非空字符不是数字，或者str为空或str只有空格字符，视为非法
If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
如果非法，返回0，如果正确的数字超出了表示范围，则返回INT_MAX或INT_MIN
'''


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None:
            return 0
        result = 0
        # neg -- 0: 还未出现正负号，1表示正号，-1表示负号
        neg = 0
        noInt = True
        for x in xrange(0, len(str)):
            char = str[x]
            if char == ' ':
                if result != 0 or neg != 0:
                    #遇到空格，但是已经有过数字，停止遍历 
                    break
            else:
                ascii = ord(char)
                if (ascii >= 48 and ascii <= 57) or (ascii == 45) or (ascii == 43):
                    # 45 表示 - ，43 表示 +
                    if ascii == 45 or ascii == 43:
                        if noInt and neg == 0:
                            neg = 1 if ascii == 43 else -1
                        else:
                            break
                    else:
                        noInt = False
                        result = result * 10 + ascii - 48
                else:
                    if result != 0:
                        break
                    else:
                        return 0
        result = result if neg != -1 else -result
        result = 2147483647 if result > 2147483647 else result
        result = -2147483648 if result < -2147483648 else result
        return result


print Solution().myAtoi("    -21474836480")



















