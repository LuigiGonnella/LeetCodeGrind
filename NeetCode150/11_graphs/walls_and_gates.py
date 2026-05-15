
#!O((R*C)^2)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0]) if grid else 0
        INF = 2147483647
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            
            queue = deque([(r, c)])
            distance = 0 #i can have a global distance to increase only after a level (inner for) or i can have a distance array and track the minimum as best distance
            visited = [[False] * COLS for _ in range(ROWS)] 
            visited[r][c] = True

            while queue:
                
                for _ in range(len(queue)):
                    currR, currC = queue.popleft()
                    for rn, cn in neighbors:
                        new_r = currR + rn
                        new_c = currC + cn

                        if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] >= 0:
                            if not visited[new_r][new_c]:
                                visited[new_r][new_c] = True
                                queue.append([new_r, new_c])
                        
                                if grid[new_r][new_c] == 0:
                                    grid[r][c] = distance + 1
                                    return
                distance += 1
            
        #!O((R*C)^2)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    bfs(r, c)


#MULTI-SOURCE BFS
#we run the BFS from each TREASURE simultaneusly and we track the distance to reach avery other INF node
#!O(R*C)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        queue = deque()
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited[r][c] = True
        
        distance = 1

        while queue:
            for _ in range(len(queue)): #visito di 1 in 1 tutti i vicini, quindi se ne trovo uno --> distaza per forza minima
            #inizio con i nodi distanziati 1, poi vado a quelli distanziati 2, ecc...
                r, c = queue.popleft()
                for rn, cn in neighbors:
                    new_r = r + rn
                    new_c = c + cn
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] > 0 and not visited[new_r][new_c]:
                            visited[new_r][new_c] = True
                            queue.append([new_r, new_c])
                            grid[new_r][new_c] = distance
            distance += 1



        
