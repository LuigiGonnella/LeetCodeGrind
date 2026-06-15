
#!O(M*N) time and O(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS = len(matrix)
        COLS = len(matrix[0]) if matrix else 0

        def setColRow(r, c):

            for j in range(COLS):
                if j != c and matrix[r][j] != 0:
                    matrix[r][j] = "*"
            
            for i in range(ROWS):
                if i != r and matrix[i][c] != 0:
                    matrix[i][c] = "*"
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    setColRow(i, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        
        