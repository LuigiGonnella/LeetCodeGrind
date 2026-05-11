
#! ADJACENCY LIST DFS --> O(V + E) --> number of ones + 4 --> O(number of 1)
#!but here we are visiting each element of the matrix in the double loop --> O(M*N)
class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0]) if grid else 0 
        cc = 0

        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            
            grid[r][c] = '0'

            for rn, cn in neighbours:
                new_r = r + rn
                new_c = c + cn
                if (new_r  >= 0) and (new_r < ROWS) and (new_c >= 0) and (new_c < COLS) and grid[new_r][new_c] != '0':
                    dfs(new_r, new_c)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != '0':
                    cc += 1
                    dfs(r, c)
        
        return cc
        