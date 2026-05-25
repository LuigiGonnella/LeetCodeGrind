
#!O(2^N) time and O(N) space
#RECURSION
class Solution:
    def numDistinct(self, s: str, t: str) -> int:   
        n = len(s)
        m = len(t)

        if m > n:
            return 0

        def dfs(i, j): #N

            if j == m:
                return 1

            if i == n:
                return 0

            res = dfs(i + 1, j) #number of subsequences without taking i
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)  #number of subsequences taking i

            return res #return both cases
        
        return dfs(0, 0)
    

#!O(N*M) time and O(N*M) space
#TOP-DOWN, memoization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:   
        n = len(s)
        m = len(t)

        if m > n:
            return 0
        
        memo = [[-1] * m for _ in range(n)] 

        def dfs(i, j): #N

            if j == m:
                return 1

            if i == n:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]

            res = dfs(i + 1, j) #number of subsequences without taking i
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)  #number of subsequences taking i

            memo[i][j] = res
            return res #return both cases
        
        return dfs(0, 0)

#!O(N*M) time and O(N*M) space
#BOTTOM-UP
class Solution:
    def numDistinct(self, s: str, t: str) -> int:   
        n = len(s)
        m = len(t)

        if m > n:
            return 0
        
        dp = [[0] * (m + 1) for _ in range(n + 1)] #(i, j) contains the number of solutions until i char of s and j char of t
        
        for i in range(n + 1):
            dp[i][m] = 1

        for i in range (n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        
        return dp[0][0]

#!O(N*M) time and O(M) space
#BOTTOM-UP
class Solution:
    def numDistinct(self, s: str, t: str) -> int:   
        n = len(s)
        m = len(t)

        if m > n:
            return 0
        
        dp = [0] * (m + 1)  #(i, j) contains the number of solutions until i char of s and j char of t
        dp_next = [0] * (m + 1) 

        dp[m] = 1
        dp_next[m] = 1

        for i in range (n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[j] = dp_next[j]
                if s[i] == t[j]:
                    dp[j] += dp_next[j + 1]
            
            dp_next = dp[:]

        return dp_next[0]


#!O(N*M) time and O(M) space
#BOTTOM-UP
class Solution:
    def numDistinct(self, s: str, t: str) -> int:   
        n = len(s)
        m = len(t)

        if m > n:
            return 0
        
        dp = [0] * (m + 1)  #(i, j) contains the number of solutions until i char of s and j char of t
        dp[m] = 1

    

        for i in range (n - 1, -1, -1):
            prev = 1
            for j in range(m - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev
            
            prev = dp[j]
            dp[j] = res

        return dp[0]
        