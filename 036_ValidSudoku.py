# coding:utf-8
# @sinner
# 16/8/19

'''
36. Valid Sudoku  QuestionEditorial Solution  My Submissions
Total Accepted: 85536
Total Submissions: 266441
Difficulty: Easy
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowValid = [[False for i in range(9)] for j in range(9)]
        columnValid = [[False for i in range(9)] for j in range(9)]
        subBoardValid = [[False for i in range(9)] for j in range(9)]

        for x in xrange(0, 9):
            for y in xrange(0, 9):
                char = board[x][y]
                if char != '.':
                    num = int(char) - 1
                    if rowValid[x][num]:
                        return False
                    else:
                        rowValid[x][num] = True
                    if columnValid[y][num]:
                        return False
                    else:
                        columnValid[y][num] = True
                    i = x - x % 3 + y / 3
                    # j = x % 3 * 3 + y % 3
                    if subBoardValid[i][num]:
                        return False
                    else:
                        subBoardValid[i][num] = True
        return True


print Solution().isValidSudoku([".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........", "9........"])






