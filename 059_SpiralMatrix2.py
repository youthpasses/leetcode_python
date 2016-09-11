# coding:utf-8
# @sinner
# 16/9/6

'''
59. Spiral Matrix II  QuestionEditorial Solution  My Submissions
Total Accepted: 61811
Total Submissions: 168778
Difficulty: Medium
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
# import numpy as np


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        # res = np.ones((n, n), dtype=int)
        res = [[0 for j in range(n)] for i in range(n)]
        circle = 0
        i = 0
        x = 0
        y = 0
        j = 2
        res[0][0] = 1
        while j <= n * n:
            circle = i / 4
            if i % 4 == 0:
                if x < n - circle - 1:
                    x += 1
                    res[y][x] = j
                    j += 1
                else:
                    i += 1
                    continue
            elif i % 4 == 1:
                if y < n - circle - 1:
                    y += 1
                    res[y][x] = j
                    j += 1
                else:
                    i += 1
                    continue
            elif i % 4 == 2:
                if x > circle:
                    x -= 1
                    res[y][x] = j
                    j += 1
                else:
                    i += 1
                    continue
            else:
                if y > circle + 1:
                    y -= 1
                    res[y][x] = j
                    j += 1
                else:
                    i += 1
        return res

print Solution().generateMatrix(4)



