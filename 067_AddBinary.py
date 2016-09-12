# coding:utf-8
# @sinner
# 16/9/12

'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1 = list(a) if len(a) > len(b) else list(b)
        l2 = list(b) if len(a) > len(b) else list(a)
        l1 = [int(x) for x in l1]
        l2 = [int(x) for x in l2]
        jinwei = 0
        dis = abs(len(a) - len(b))
        for i in xrange(len(l1) - 1, -1, -1):
            j = i - dis
            if j > -1:
                if l1[i] == 0 and l2[j] == 0:
                    l1[i] = jinwei
                    jinwei = 0
                elif (l1[i] == 1 and l2[j] == 0) or (l1[i] == 0 and l2[j] == 1):
                    l1[i] = 1 if jinwei == 0 else 0
                    jinwei = 0 if jinwei == 0 else 1
                else:
                    l1[i] = 1 if jinwei == 1 else 0
                    jinwei = 1
            else:
                l1[i] = jinwei if l1[i] == 0 else 0 if jinwei == 1 else 1
                jinwei = 1 if l1[i] == 0 and jinwei == 1 else 0
        if jinwei == 1:
            l1.insert(0, 1)
        l1 = [str(x) for x in l1]
        return ''.join(l1)

print Solution().addBinary("1010", '1011')
            