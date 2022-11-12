import os
import sys

"""
Runtime: 227 ms, faster than 42.16% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 35.53% of Python3 online submissions for Valid Sudoku.
"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        flipped_board = [list(x) for x in list(zip(*board))]
        squares = []
        for i in (0, 3, 6):
                for j in (0, 3, 6):
                    squares.append([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)])

        for row in board + flipped_board + squares:
            clean_row = [el for el in row if el != '.']
            if len(set(clean_row)) != len(clean_row):
                return False

        return True




def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	res = solution.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
	print(res)