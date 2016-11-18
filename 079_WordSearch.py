# coding:utf-8
# @sinner
# 16/11/7

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
    	m = len(board)
    	n = len(board[0])
    	for i in xrange(0, m):
    		for j in xrange(0, n):
    			if board[i][j] == word[0]:
    				visited = [[False for x in xrange(n)] for y in xrange(m)]
    				res = self.bt(board, word, i, j, 0, visited)
    				if res:
    					return res
    	return False

    def bt(self, board, word, x, y, i, visited):
    	if i == len(word):
    		return True
    	if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
    		return False
    	if visited[x][y]:
    		return False
    	if board[x][y] != word[i]:
    		return False
    	visited[x][y] = True
    	exist = self.bt(board, word, x - 1, y, i + 1, visited) or self.bt(board, word, x + 1, y, i + 1, visited) or self.bt(board, word, x, y - 1, i + 1, visited) or self.bt(board, word, x, y + 1, i + 1, visited)
    	visited[x][y] = False
    	return exist

print Solution().exist(["ABCE","SFES","ADEE"], "ABCESEEEFS")