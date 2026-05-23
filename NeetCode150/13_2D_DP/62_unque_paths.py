

#!O(2^(m + n)) time and O(M + N) space
#RECURSION
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(i, j):

            if i == 0 and j == 0:
                return 1 #valid
            
            if i < 0 or j < 0:
                return 0 #not valid
            
            return dfs(i - 1, j) + dfs(i, j - 1)
        
        return dfs(m - 1, n - 1)


#!O(M*N) time and space
#TOP-DOWN
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):

            if i == 0 and j == 0:
                return 1 #valid
            
            if i < 0 or j < 0:
                return 0 #not valid
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = dfs(i - 1, j) + dfs(i, j - 1)
            return memo[i][j]
        
        return dfs(m - 1, n - 1)




#!O(M*N) time and space
#BOTTOM-UP 2D
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] += (dp[i - 1][j] + dp[i][j - 1])
        
        return dp[m][n]

#!O(M*N) time and O(N) space
#BOTTOM-UP 1D
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        curr_row = [0] * (n + 1) 
        prev_row = [0] * (n + 1) 
        curr_row[1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_row[j] = (curr_row[j] + (prev_row[j] + curr_row[j - 1])) if (i == 1 and j == 1) else (prev_row[j] + curr_row[j - 1])
            
            curr_row, prev_row = prev_row, curr_row #switch because we overwrite everytime the current "curr_row"
        
        return prev_row[n]




        