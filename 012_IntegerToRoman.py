# coding:utf-8
# @sinner
# 16/6/16


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        q = num / 1000
        left = num % 1000
        for i in xrange(0, q):
            roman += 'M'

        b = left / 100
        left = left % 100
        print b
        if b <= 3:
            for i in xrange(0, b):
                roman += 'C'
        elif b == 4:
            roman += 'CD'
        elif b <= 8:
            roman += 'D'
            for i in xrange(5, b):
                roman += 'C'
        else:
            roman += 'CM'

        s = left / 10
        left = left % 10
        if s <= 3:
            for i in xrange(0, s):
                roman += 'X'
        elif s == 4:
            roman += 'XL'
        elif s <= 8:
            roman += 'L'
            for i in xrange(5, s):
                roman += 'X'
        else:
            roman += 'XC'

        if left <= 3:
            for i in xrange(0, left):
                roman += 'I'
        elif left == 4:
            roman += 'IV'
        elif left <= 8:
            roman += 'V'
            for i in xrange(5, left):
                roman += 'I'
        else:
            roman += 'IX'
        return roman

print Solution().intToRoman(100)
