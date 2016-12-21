# coding:utf-8
# @sinner
# 16/11/20

'''
463. Island Perimeter My SubmissionsBack To Contest
User Tried: 0
Total Submissions: 0
Difficulty: Easy
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid[0])
        h = len(grid)
        res = 0
        for x in xrange(0, h):
        	for y in xrange(0, w):
        		if grid[x][y] == 1:
        			if x == 0 or grid[x - 1][y] != 1:
        				res += 1
        			if x == h - 1 or grid[x + 1][y] != 1:
        				res += 1
        			if y == 0 or grid[x][y - 1] != 1:
        				res += 1
        			if y == w - 1 or grid[x][y + 1] != 1:
        				res += 1
    	return res

print Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])