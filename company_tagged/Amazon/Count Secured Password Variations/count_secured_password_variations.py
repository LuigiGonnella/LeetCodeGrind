

#BRUTE FORCE
#!O(N * 2 ^ N) time and O(N) space
# class Solution:

#     def CountSecuredPassword(s: str, t: str) -> int:

#         n = len(s)
#         curr_sol = []
#         n_sol = 0

#         def dfs(i):
#             nonlocal n_sol

#             if i == n:
#                 n_sol += 1 if "".join(curr_sol) > t else 0 #!this join gives the additional N complexity
#                 return


#             curr_sol.append(s[i])
#             dfs(i + 1)
#             curr_sol.pop()
#             dfs(i + 1)
        
#         dfs(0)

#         return n_sol % (1e9 +7)



#TOP-DOWN
#!O(N * M) time and space
class Solution:
    def CountSecuredPassword(self, s: str, t: str) -> int:
        mod = 10**9 + 7
        m = len(t)
        n = len(s)

        pow_2 = [1] * n

        memo = [[-1] * m for _ in range(n)]

        for i in range(1, n): 
            pow_2[i] = (pow_2[i - 1] * 2) % mod #O(1) lookup to obtain power of 2 capped to mod so we don't risk 2 ** n overflows

        def dfs(i, j): #for every char/sunsequence of s BIGGER than t --> add all next possible sunsequence to solutiom\
            
            #since we only move j where a perfect match occur, now we matched all t --> every combination of remaining chars in s makes that subsequence > t
            if j == m:
                remaining_chars = n - i
                return pow_2[remaining_chars] - 1 #exclude the perfect match
            
            if i == n: #we processed all s without a solution
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            #!HOW MANY WAYS OF BUILDING A BIGGER SUBSEQUENCE THAN t IN s STARTING FROM i having matched t until j - 1 WE HAVE?

            #CASE 1: EXCLUDE IT
            ways = dfs(i + 1, j)

            #IF WE CAN INCLUDE IT
            if s[i] > t[j]: #CASE 2: instant win
                remaining_chars = n - i - 1 #exclude the current
                ways += pow_2[remaining_chars] 

            elif s[i] == t[j]: #CASE 2: continue the matching streak
                ways += dfs(i + 1, j + 1)
            
            memo[i][j] = ways
            return ways


        return dfs(0, 0)

#BOTTOM-UP
#!O(N * M) time and space
class Solution:
    def CountSecuredPassword(self, s: str, t: str) -> int:
        mod = 10**9 + 7
        m = len(t)
        n = len(s)

        pow_2 = [1] * (n + 1)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n): 
            pow_2[i] = (pow_2[i - 1] * 2) % mod #O(1) lookup to obtain power of 2 capped to mod so we don't risk 2 ** n overflows

        for i in range(n + 1):
            remaining_chars = n - i
            dp[i][m] = pow_2[remaining_chars] - 1 

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] 

                if s[i] > t[j]: #CASE 2: instant win
                    remaining_chars = n - i - 1 #exclude the current
                    dp[i][j] += pow_2[remaining_chars] 

                elif s[i] == t[j]: #CASE 2: continue the matching streak
                    dp[i][j] += dp[i + 1][j + 1]
                
                dp[i][j] %= mod
                
                
        
        return dp[0][0]