
#!O(2 ^ (M + N)) time and O(M + N) space
#RECURSION
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        def dfs(i, j):

            if j == m:
                return i == n
              
            
            match = i < n and (s[i] == p[j] or p[j] == ".")
            
            if j < m - 1 and p[j + 1] == "*":
                return (dfs(i, j + 2) #skip char*
                or (match and dfs(i + 1, j))) #if s[i] == p[j] we can take and continue
            
            if match: #if we placed this statement before the previous one (checking the * char) we would never land that statement, since if the char before * match the current s[i] char, we would always return dfs(i+1, j+1)!!
                return dfs(i + 1, j + 1)

            return False
        
        return dfs(0, 0)

#!O((M*N)) time and space
#RECURSION      
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        memo = [[-1] * m for _ in range(n)]

        def dfs(i, j):

            if j == m:
                return i == n
            
            if i < n and memo[i][j] != -1:
                return memo[i][j]
              
            
            match = i < n and (s[i] == p[j] or p[j] == ".")
            
            if j < m - 1 and p[j + 1] == "*":
                res = (dfs(i, j + 2) #skip char*
                or (match and dfs(i + 1, j))) #if s[i] == p[j] we can take and continue

                if i < n:
                    memo[i][j] = res
                return res
            
            if match:
                res = dfs(i + 1, j + 1)
                if i < n:
                    memo[i][j] = res
                
                return res
            
            if i < n:
                memo[i][j] = False

            return False
        
        return dfs(0, 0)

#!O((M *N)) time and space
#BOTTOM-UP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        dp = [[False] * (m + 1) for _ in range(n + 1)] #(i, j) says if we can match s[i:] with p[j:]


        dp[n][m] = True #we finshed the pattern AND the string

        for i in range(n, -1, -1): #we have to process i = n too
            for j in range(m - 1, -1, -1): #j = m is already fixed in dp (True only in i = n row)
                match = i < n and (s[i] == p[j] or p[j] == ".")
                if j < (m - 1) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or ( #here we understand why it is important ot start with i = n --> in dp[n][j] we will place True if j + 1 is * and dp[n][j] si True (e.g. dp[n][m])
                        (match) and
                        dp[i + 1][j]
                    )
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]
                
        
        return dp[0][0]
    

#!O((M *N)) time and O(m) space
#BOTTOM-UP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        dp = [False] * (m + 1) #(i, j) says if we can match s[i:] with p[j:]
        dp[m] = True #we finshed the pattern AND the string

        

        for i in range(n, -1, -1): #we have to process i = n too
          nextDp = [False] * (len(p) + 1)
          nextDp[len(p)] = (i == len(s))

            for j in range(m - 1, -1, -1): #j = m is already fixed in dp (True only in i = n row)
                match = i < n and (s[i] == p[j] or p[j] == ".")
                if j < (m - 1) and p[j + 1] == "*":
                    next_dp[j] = next_dp[j + 2] or ( #here we understand why it is important ot start with i = n --> in dp[n][j] we will place True if j + 1 is * and dp[n][j] si True (e.g. dp[n][m])
                        (match) and
                        dp[j]
                    )
                elif match:
                    next_dp[j] = dp[j + 1]
            
            dp = next_dp
                
        
        return dp[0]



#!O((M *N)) time and O(m) space
#BOTTOM-UP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        dp = [False] * (m + 1) #(i, j) says if we can match s[i:] with p[j:]
        dp[m] = True
          

        for i in range(n, -1, -1): #we have to process i = n too
            dp1 = dp[m]
            dp[m] = i == n #we finshed the pattern AND the string

            for j in range(m - 1, -1, -1): #j = m is already fixed in dp (True only in i = n row)
                match = i < n and (s[i] == p[j] or p[j] == ".")
                res = False
                if j < (m - 1) and p[j + 1] == "*":
                    res = dp[j + 2] or ( #here we understand why it is important ot start with i = n --> in dp[n][j] we will place True if j + 1 is * and dp[n][j] si True (e.g. dp[n][m])
                        (match) and
                        dp[j]
                    )
                elif match:
                    res = dp1
            
                dp[j], dp1 = res, dp[j]
                
        
        return dp[0]

