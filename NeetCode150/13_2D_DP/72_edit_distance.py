

#!O(3^(M+N)) time and O(M+N) space
#RECURSION
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        def dfs(i, j):
            if j == m: #if only word2 finished --> we need to delete all remaining after i in word1 (we added until match inside word1)
                return n - i
            
            if i == n: #if only word1 finished --> we need to delete all remaining after j in word2 (we deleted/replaced unti match in word1)
                return m - j
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            
            return min( 
                    1+ dfs(i, j + 1), #INSERT
                    1+ dfs(i + 1, j), #DELETE
                    1+ dfs(i + 1, j + 1) #REPLACE
                )
            
        
        return dfs(0, 0)
                

#!O(M*N) time and space
#MEMOIZATION
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        memo = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if j == m: #if only word2 finished --> we need to delete all remaining after i in word1 (we added until match inside word1)
                return n - i
            
            if i == n: #if only word1 finished --> we need to delete all remaining after j in word2 (we deleted/replaced unti match in word1)
                return m - j
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            if word1[i] == word2[j]:
                memo[i][j] = dfs(i + 1, j + 1)
                return memo[i][j]
            
            
            memo[i][j] = min( 
                    1+ dfs(i, j + 1), #INSERT
                    1+ dfs(i + 1, j), #DELETE
                    1+ dfs(i + 1, j + 1) #REPLACE
                )
            return memo[i][j]
            
        
        return dfs(0, 0)


#!O(M*N) time and space
#BOTTOM-UP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[float("+inf")] * (m + 1) for _ in range(n + 1)] #keeps track of minimum distance between words until (i, j)

        for j in range(m + 1): #when i finished word1 but i am at j for word2 --> add missing m - j
            dp[n][j] = m - j
        
        for i in range(n + 1):#when i finished word2 but i am at i in word1 --> delete missing n - i
            dp[i][m] = n - i

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        1 + dp[i + 1][j], #delete
                        1 + dp[i][j + 1], #insert
                        1 + dp[i + 1][ j + 1] #insert
                    )
        
        return dp[0][0]

        
        
    



#!O(M*N) time and O(min(M, N) space
#BOTTOM-UP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if m < n: #word1 (n) is shortest
            n, m = m, n
            word1, word2 = word2, word1


        dp = [float("+inf")] * (m + 1)  #keeps track of minimum distance between words until (i, j)
        next_dp = [float("+inf")] * (m + 1)
        for j in range(m + 1): #when word1 is finished, add the remaining to match word2
            dp[j] = m - j
        

        for i in range(n - 1, -1, -1):
            next_dp[m] = n - i #when word2 is finished, delete from match1
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    next_dp[j] = dp[j + 1]
                else:
                    next_dp[j] = min(
                        1 + dp[j], #delete
                        1 + next_dp[j + 1], #insert
                        1 + dp[j + 1] #insert
                    )
                
            dp = next_dp[:]
        
        return dp[0]























