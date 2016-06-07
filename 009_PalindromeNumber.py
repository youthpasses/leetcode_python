# coding:utf-8
# @sinner
# 16/6/5

'''
Total Accepted: 126961 Total Submissions: 396130 Difficulty: Easy
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if len(str(x)) == 1:
            return True
        length = len(str(x))
        for i in xrange(0, length / 2):
            x1 = (x % (10 ** (i + 1))) / (10 ** i)
            x2 = (x % (10 ** (length - i))) / (10 ** (length - 1 - i))
            if x1 != x2:
                return False
        return True


print Solution().isPalindrome(1200100210)









