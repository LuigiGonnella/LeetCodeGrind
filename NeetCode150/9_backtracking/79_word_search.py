
#O(R*C*4^L) L = length of the word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0]) if board else 0
        found = False

        def dfs(r, c, idx) -> bool:
            if idx >= len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[idx]:
                return False
            
            board[r][c] = "*"

            inner = (dfs(r - 1, c, idx + 1) or dfs(r + 1, c, idx + 1)
                    or dfs(r, c - 1, idx + 1) or dfs(r, c + 1, idx + 1))
            
            board[r][c] = word[idx] #backtrack
            
            return inner
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
            
            
            
            

            

        