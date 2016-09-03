# coding:utf-8
# @sinner
# 16/9/3

'''
54. Spiral Matrix  QuestionEditorial Solution  My Submissions
Total Accepted: 70364
Total Submissions: 297890
Difficulty: Medium
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])
        circle = 0
        i = 0
        x = 0
        y = 0
        res = [matrix[0][0]]
        while True:
            circle = i / 4
            if i % 4 == 0:
                if x < n - circle - 1:
                    x += 1
                    #print y, x
                    res.append(matrix[y][x])
                else:
                    i += 1
                    continue
            elif i % 4 == 1:
                if y < m - circle - 1:
                    y += 1
                    res.append(matrix[y][x])
                else:
                    i += 1
                    continue
            elif i % 4 == 2:
                if x > circle:
                    x -= 1
                    res.append(matrix[y][x])
                else:
                    i += 1
                    continue
            elif i % 4 == 3:
                if y > circle + 1:
                    y -= 1
                    res.append(matrix[y][x])
                else:
                    i += 1
            else:
                pass
            if len(res) == m * n:
                break
        return res

print Solution().spiralOrder([])
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]


