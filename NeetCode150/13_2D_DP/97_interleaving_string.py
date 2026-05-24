

#!((L2 + L1)^3) time and space --> wrong approach, tries to check every possible slice
#TOP-DOWN
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        l1 = len(s1)
        l2 = len(s2)

        s1_visited = []
        s2_visited = []

        memo = {}

        def dfs(i, start1, start2):

            if i == n:
                if abs(len(s1_visited) - len(s2_visited)) > 1:
                    return False

                return "".join(s1_visited) == s1 and  "".join(s2_visited) == s2
            
            if (i, start1, start2) in memo:
                return memo[(i, start1, start2)]


            for j in range(i, n):
                l = j - i + 1
                if start1 < l1 and s3[i: j + 1] == s1[start1:start1 + l]:
                    s1_visited.append(s3[i: j + 1])

                    if dfs(j + 1, start1 + l , start2):
                        memo[(i, start1, start2)] = True
                        return True
                
                    s1_visited.pop()
                if start2 < l2 and s3[i: j + 1] == s2[start2:start2 + l]:
                    s2_visited.append(s3[i: j + 1])

                    if dfs(j + 1, start1, start2 + l):
                        memo[(i, start1, start2)] = True
                        return True
                    s2_visited.pop()

            memo[(i, start1, start2)] = False
            return False
        
        return dfs(0, 0, 0)



#!O(2 ^ (L1 + L2)) time and (L1 + L2) space
#RECURSION
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        l1 = len(s1)
        l2 = len(s2)


        def dfs(i, j):

            if i + j == n: #check coverage (|n - m| <= 1 matematically respected)
                return i == l1 and j == l2

            if i < l1 and s3[i + j] == s1[i] and dfs(i + 1, j):
                return True
            
            if j < l2 and s3[i + j] == s2[j] and dfs(i, j + 1):
                return True
            
            return False
        
        return dfs(0, 0)
            
#!O(L1 * L2) time and space
#RECURSION
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        l1 = len(s1)
        l2 = len(s2)

        memo = [[-1] * (l1 + 1) for _ in range(l2 + 1)] #state is already defined by j and k, we can exclude i (always equal to i or j)

        def dfs(i, j):

            if i + j == n: #check coverage (|n - m| <= 1 matematically respected)
                return j == l1 and i == l2
            
            if memo[i][j] != -1:
                return memo[i][j]

            if j < l1 and s3[i + j] == s1[j] and dfs(i, j + 1):
                memo[i][j] = True
                return True
            
            if i < l2 and s3[i + j] == s2[i] and dfs(i + 1, j,):
                memo[i][j] = True
                return True
            
            memo[i][j] = False
            return False
        
        return dfs(0, 0)
        

#!O(L1 * L2) time and O(L1 *L2) space
#BOTTOM-UP
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
            
#!O(L1 * L2) time and O(min(L1, L2)) space
#BOTTOM-UP
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        l1 = len(s1)
        l2 = len(s2)

        if l1 + l2 != n:
            return False


        if l2 < l1:
            s1, s2 = s2, s1
            l1, l2 = l2, l1 #l1 min

        
        dp = [False] * (l2 + 1) #true if i can form s3[i + j:] using s2[i:] and s1[j:]
        dp[l2] = True


        for i in range(l1, -1, -1):
            next_dp = [False] * (l2 + 1)
            if i == l1:
                next_dp[l2] = True
            for j in range(l2, -1, -1):
                if i < l1 and s1[i] == s3[i + j] and dp[j]:
                    next_dp[j] = True
                
                if j < l2 and s2[j] == s3[i + j] and next_dp[j + 1]:
                    next_dp[j] = True
            
            dp = next_dp


        return dp[0]      






