# coding:utf-8
# @sinner
# 16/8/20

'''
37. Sudoku Solver  QuestionEditorial Solution  My Submissions
Total Accepted: 55847
Total Submissions: 212666
Difficulty: Hard
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0)
        print board

    def solve(self, board, index):
        if index == 81:
            return True
        else:
            x = index / 9
            y = index % 9
            if board[x][y] == '.':
                for c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if self.isValid(board, x, y, c):
                        board[x][y] = c
                        if self.solve(board, index + 1):
                            return True
                        else:
                            board[x][y] = '.'
                return False
            else:
                if self.solve(board, index + 1):
                    return True
        return False

    def isValid(self, board, x, y, c):
        for j in xrange(0, 9):
            m = x / 3 * 3 + j / 3
            n = y / 3 * 3 + j % 3
            if board[j][y] == c or board[x][j] == c or board[m][n] == c:
                return False
        return True

Solution().solveSudoku(["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."])


'''
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self.solve(board)

    def solve(self, board):
        for row in xrange(9):
            for col in xrange(9):
                if board[row][col] == '.':
                    for c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        if self.unvalid(board, row, col, c):
                            board[row] = board[row][:col] + c + board[row][col + 1:]
                            if self.solve(board):
                                return True
                            else:
                                board[row] = board[row][:col] + '.' + board[row][col + 1:]
                    return False
        return True

    def unvalid(self, board, x, y, c):
        for j in xrange(0, 9):
            m = x / 3 * 3 + j / 3
            n = y / 3 * 3 + j % 3
            if board[j][y] == c or board[x][j] == c or board[m][n] == c:
                return False
        return True
'''


