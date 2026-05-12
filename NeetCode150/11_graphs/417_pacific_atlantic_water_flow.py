
#!O(R*C)
#BFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0]) if heights else 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        

        def bfs(r, c, visited):
            q = deque([(r, c)])
            visited.add((r, c))

            while q:
                currR, currC = q.popleft()

                for nr, nc in neighbors:
                    newR = currR + nr
                    newC = currC + nc

                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and heights[newR][newC] >= heights[currR][currC] and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        q.append((newR, newC))

        


        visitedPac = set()
        visitedAtl = set()

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    bfs(r, c, visitedPac)
                if r == (ROWS - 1) or c == (COLS - 1):
                    bfs(r, c, visitedAtl)
        
        return [list(el) for el in (visitedPac & visitedAtl)]


#!O(R*C)
#DFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0]) if heights else 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):

            visited.add((r, c))

            for nr, nc in neighbors:
                newR = r + nr
                newC = c + nc

                if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and heights[newR][newC] >= heights[r][c] and (newR, newC) not in visited:
                    dfs(newR, newC, visited)

        visitedPac = set()
        visitedAtl = set()

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r, c, visitedPac)
                if r == (ROWS - 1) or c == (COLS - 1):
                    dfs(r, c, visitedAtl)
        
        return [list(el) for el in (visitedPac & visitedAtl)]
