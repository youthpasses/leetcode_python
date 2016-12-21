# coding:utf-8
# @makai
# 16/12/11

'''
474. Ones and Zeroes

    User Accepted: 147
    User Tried: 293
    Total Accepted: 150
    Total Submissions: 699
    Difficulty: Medium

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

    The given numbers of 0s and 1s will both not exceed 100
    The size of given string array won't exceed 600.

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[0 for x in xrange(n + 1)] for y in xrange(m + 1)]
        for i in xrange(1, len(strs) + 1):
        	s = strs[i - 1]
        	c0, c1 = self.getCountOf0and1(s)
        	for x in xrange(m, -1, -1):
        		for y in xrange(n, -1, -1):
        			if x - c0 >= 0 and y - c1 >= 0:
	        			f[x][y] = max(f[x - c0][y - c1] + 1, f[x][y])
        return f[m][n]

    def getCountOf0and1(self, number):
    	c0 = 0
    	c1 = 0
    	for char in number:
    		if char == '0':
    			c0 += 1
    		else:
    			c1 += 1
    	return c0, c1

print Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)