
#!O(4^(M*N)) time and O(M*N) space
#DFS
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0]) if matrix else 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = -1

        def dfs(r, c, currLen): #N^2
            nonlocal res            

            for rn, cn in neighbors:
                newR = r + rn
                newC = c + cn

                if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and matrix[newR][newC] > matrix[r][c] :
                    dfs(newR, newC, currLen + 1)
            
            res = max(res, currLen)
        
        #N
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, 1)

        return res


#!O(4^(M*N)) time and O(M*N) space
#BFS
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0]) if matrix else 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = -1

        def bfs(r, c):
            q = deque([(r, c)])
            currLen = 0

            while q:
                for _ in range(len(q)):
                    currR, currC = q.popleft()
                    for nr, nc in neighbors:
                        newR = currR + nr
                        newC = currC + nc

                        if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and matrix[newR][newC] > matrix[currR][currC]:
                            q.append((newR, newC))
                currLen += 1
            
            return currLen
                    
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(bfs(r, c), res)


        return res

#!O(M*N) time and space
#DFS TOP-DOWN, memoization
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0]) if matrix else 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        memo = [[-1] * COLS for _ in range(ROWS)]
        res = 0

        def dfs(r, c): #N^2

            if memo[r][c] != -1:
                return memo[r][c]           

            currLen = 1
            for rn, cn in neighbors:
                newR = r + rn
                newC = c + cn

                if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and matrix[newR][newC] > matrix[r][c] :
                    currLen = max(currLen, 1 + dfs(newR, newC))
            
            memo[r][c] = currLen
            return memo[r][c]
        
        #N
        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r, c), res)

        return res  

#!O(M*N) time and space
#KAHN'S ALGORITHM --> the problem makes the GRID a logical DAG (smaller number --> bigger number) --> avoid visiting useless nodes, avoid backtracking
#push to q only if in_degree = 0 --> no duplicate work (in normal BFS we push every time we find (r, c))

#visit each CELL ones and each neighbor once --> O(M * N) time and space
#in a DAG, the longest possile path is found processing the nodes in topological order (KAHN)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0]) if matrix else 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        in_degree = [[0] * COLS for _ in range(ROWS)]
        
        #COMPUTE IN_DEGREE
        for r in range(ROWS):
            for c in range(COLS):
                for rn, cn in neighbors:
                    newR = r + rn
                    newC = c + cn

                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and matrix[newR][newC] > matrix[r][c]:
                        in_degree[newR][newC] += 1
        
        q = deque()

        #ADD SOURCE TO QUEUE
        for r in range(ROWS):
            for c in range(COLS):
                if not in_degree[r][c]:
                    q.append((r, c))
        
        #VISIT BY LEVEL (height = longest path)
        maxLen = 0
        while q:
            maxLen += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for rn, cn in neighbors:
                    newR = r + rn
                    newC = c + cn
                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and matrix[newR][newC] > matrix[r][c] :
                        in_degree[newR][newC] -= 1 
                        if not in_degree[newR][newC]:
                            q.append((newR, newC))

        return maxLen  

