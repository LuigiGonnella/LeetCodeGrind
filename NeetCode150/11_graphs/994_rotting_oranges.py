
#!O(V + E) = O(R*C)
#both timne and space
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0]) if grid else 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        q = deque()
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        if not fresh:
            return minutes
        if len(q) == 0:
            return -1

        
        #BFS
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for rn, cn in neighbors:
                    new_r = r + rn
                    new_c = c + cn

                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] == 1:
                        fresh -= 1
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
            
            minutes += 1
        
        if fresh:
            return -1
        
        return minutes - 1

#we could have also ran the BFS from every rotten node while there are still fresh nodes, without the queue and by marking the newly rotten nodes as 3 
#so that they are not being considered as rotten in the same minute
#at the end of a minute we convert these 3 to 2 and go onto the next

#!O((R*C)^2) time but O(1) extra space (no queue)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0:
            flag = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            row, col = r + dr, c + dc
                            if (row in range(ROWS) and
                                col in range(COLS) and
                                grid[row][col] == 1):
                                grid[row][col] = 3
                                fresh -= 1
                                flag = True

            if not flag:
                return -1

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1

        return time



        