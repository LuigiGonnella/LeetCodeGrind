
# #!O(ElogE) = O(N^2logN^2) = O(N^2logN) in this case
# #MY SOLUTION
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0]) if grid else 0

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = [(grid[0][0], (0, 0))]
        distances = {}
        distances[(0, 0)] = grid[0][0]


        while pq:

            time, (r, c) = heapq.heappop(pq)

            if time > distances[(r, c)]: #instead of change priority when we insert, we skip when we read
                continue
            
            if r == (ROWS - 1) and c == (COLS - 1):
                return time
            
            for rn, cn in neighbors:
                newR = r + rn
                newC = c + cn

                if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS:
                    cost = max(grid[newR][newC], distances[(r, c)])
                    if (newR, newC) not in distances or cost < distances[(newR, newC)]:
                        distances[(newR, newC)] = cost
                        heapq.heappush(pq, (distances[(newR, newC)], (newR, newC)))
        
# #CLEAN
class Solution:
    # Time: O(V log V) where V is ROWS * COLS
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Priority Queue stores (max_time_so_far, r, c)
        pq = [(grid[0][0], 0, 0)]
        visited = set()  
        #!DO NOT ADD TO VISITED NOW!      
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            time, r, c = heapq.heappop(pq)

            # EARLY EXIT: The first time we pop the destination, we are done
            if r == ROWS - 1 and c == COLS - 1:
                return time
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited:                    
                    # The cost to step on the next square is simply the max 
                    # of our current time and the neighbor's height
                    new_time = max(time, grid[newR][newC])
                    heapq.heappush(pq, (new_time, newR, newC))

