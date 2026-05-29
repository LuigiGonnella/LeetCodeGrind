
#!O(MxN) time and O(MxN) space
#BFS
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0]) if board else 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        processed = set() #set of processed nodes

        q = deque([(0, 0)]) #start BFS from (0, 0) node
        processed.add((0, 0))

        while q:
            live_count = 0

            r, c = q.popleft()

            for nr, nc in neighbors:
                newR = r + nr
                newC = c + nc

                if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS:
                    if board[newR][newC] == 1 or board[newR][newC] == "D":
                        live_count += 1                        
                    
                    if (newR, newC) not in processed: #we didn't processed it yet (evaluating if switch from 1 to 0, viceversa or nothing)
                        processed.add((newR, newC))
                        q.append((newR, newC))
            
            if board[r][c]:
                if live_count < 2 or live_count > 3:
                    board[r][c] = "D"
            else:
                if live_count == 3:
                    board[r][c] = "L"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "L":
                    board[r][c] = 1
                elif board[r][c] == "D":
                    board[r][c] = 0



#!O(MxN) time and O(1) space
#ITERATION
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0]) if board else 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                live_count = 0

                for nr, nc in neighbors:
                    newR = r + nr
                    newC = c + nc

                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS:
                        if board[newR][newC] == 1 or board[newR][newC] == 2: #2 means that it was live and now it is dead
                            live_count += 1
                
                if board[r][c] == 1:
                    if live_count < 2 or live_count > 3:
                        board[r][c] = 2
                else:
                    if live_count == 3:
                        board[r][c] = 3 #from dead to live
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
        