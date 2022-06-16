'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_n, col_n = len(matrix), len(matrix[0])
        row_ls, col_ls = [], []
        for row in range(row_n):
            for col in range(col_n):
                if matrix[row][col] == 0:
                    row_ls.append(row)
                    col_ls.append(col)

        for row in row_ls:
            for i in range(col_n):
                matrix[row][i] = 0
        for col in col_ls:
            for i in range(row_n):
                matrix[i][col] = 0
