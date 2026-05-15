
#! O((R*C)^2)
#DFS INSIDE-OUT
class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0]) if board else 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        

        def dfs(r, c, visited):

            if r == (ROWS - 1) or r == 0 or c == 0 or c == (COLS - 1):
                return True
            
            visited.add((r, c))

            for nr, nc in neighbors:
                newR = r + nr
                newC = c + nc

                if board[newR][newC] != "X" and (newR, newC) not in visited:
                    if dfs(newR, newC, visited):
                        return True
            
            return False
        
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] != "X":
                    visited = set()
                    if not dfs(r, c, visited):
                        board[r][c] = "X"        


#! O((R*C))
#DFS OUTSIDE-IN
class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0]) if board else 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        #visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            
            #visited[r][c] = True instead of adding memory space, we can temporarly MARK in-place the current node
            board[r][c] = "M"

            for rn, rc in neighbors:
                newR = r + rn
                newC = c + rc

                if (newR > 0 and newR < (ROWS - 1)) and (newC > 0 and newC < (COLS - 1)) and board[newR][newC] == "O":
                    dfs(newR, newC)
        
        # Check top and bottom rows
        for c in range(COLS):
            if board[0][c] == "O": dfs(0, c)
            if board[ROWS - 1][c] == "O": dfs(ROWS - 1, c)

        # Check left and right columns
        for r in range(ROWS):
            if board[r][0] == "O": dfs(r, 0)
            if board[r][COLS - 1] == "O": dfs(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "M":
                    board[r][c] = "O"


        