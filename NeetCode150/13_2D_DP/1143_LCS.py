

#!O(2^(M+N)) time and (M + N) space
#RECURSION
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        def dfs(i, j): #O(M + N)
            if i >= n or j >= m:
                return 0

            if text1[i] == text2[j]: #if we can take
                return 1 + dfs(i + 1, j + 1) #continue streak

            return max(dfs(i, j + 1), dfs(i + 1, j)) #not take

        
        return dfs(0, 0)



#!O(M*N) time and space
#TOP-DOWN, MEMOIZATION
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        memo = [[-1] * m for _ in range(n)]

        def dfs(i, j): #O(M + N)
            if i >= n or j >= m:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]

            
            if text1[i] == text2[j]: #if we can take
                memo[i][j] = 1 + dfs(i + 1, j + 1) #continue streak
            else:
                memo[i][j] = max(dfs(i, j + 1), dfs(i + 1, j)) #not take

            return memo[i][j]
        
        return dfs(0, 0)         




#!O(M * N) time and space
#BOTTOM-UP 2D
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range (1, m + 1):
            for j in range(1, n + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]  #if match --> increase streak
                else:
                    dp[i][j]  = max(dp[i][j - 1], dp[i - 1][j]) #if no match --> maintain LCS
        
        return dp[m][n]


#!O(M * N) time and O(min(M, N)) space
#BOTTOM-UP 1D
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text2) < len(text1):
            text1, text2 = text2, text1

        n = len(text1) #minimum
        m = len(text2)


        curr_row = [0] * (n + 1)
        prev_row = [0] * (n + 1)

        for i in range (1, m + 1):
            for j in range(1, n + 1):
                if text2[i - 1] == text1[j - 1]:
                    curr_row[j] = 1 + prev_row[j - 1]  #if match --> increase streak
                else:
                    curr_row[j]  = max(curr_row[j - 1], prev_row[j]) #if no match --> maintain LCS
            
            curr_row, prev_row = prev_row, curr_row
        
        return prev_row[n]




        