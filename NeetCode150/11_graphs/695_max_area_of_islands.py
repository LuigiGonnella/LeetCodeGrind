
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0]) if grid else 0

        maxArea = 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, count):
            grid[r][c] = 0

            for rn, cn in neighbors:
                new_r = r + rn
                new_c = c + cn
                if new_c >= 0 and new_c < COLS and new_r >= 0 and new_r < ROWS and grid[new_r][new_c]:
                    count = dfs(new_r, new_c, count + 1)
            
            return count
        
        for r in range(ROWS):
            for c in range(COLS): #!O(N*M)
                if grid[r][c]:
                    area = dfs(r, c, 1)
                    maxArea = max(area, maxArea)

        return maxArea        

            
            


            

        