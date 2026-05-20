
#!O(N * 2 ^ N)
#BACKTRACKING
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        n = len(s)

        def dfs(i):
            nonlocal res

            def isValid(subs):
                if subs[0] == "0" or len(subs) > 2:
                    return False

                if len(subs) == 2 and (ord(subs[0]) > ord("2")):
                    return False
                
                if len(subs) == 2 and (ord(subs[1]) > ord("6")):
                    return False

                return True

            if i == n:
                res += 1
                return

            for j in range(i, n):
                if isValid(s[i:j + 1]):
                    dfs(j + 1)
        
        dfs(0)
        
        return res
             

#!O(2^N)
#TOP-DOWN
#each character can be taken ALONE or WITH THE FOLLOWING CHARACTER
#this allows a SUMMING structure --> each CHAR can be VALID (1) or NOT VALID (0)
#going down to the RECURSION LEVELS we will see VALID PATHS made by 1 or 2 CHARS and we SUM THEM TOGETHER BACKWARDS
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        def dfs(i):
            if i == len(s): #we finished the string --> valid
                return 1
            
            if s[i] == "0": #we found a leading zero --> not valid
                return 0
            
            res = dfs(i + 1) #now that "i" is valid, we can consider the following character, this will add the current char as a valid char (inheriting the sum of next char)

            #EVALUATE COUPLE, without the following lines, we will just STOP at the first ZERO and return it (through ALL RECURSION LEVELS)
            #OR we would JUST RETURN 1 (if no zeros are found) --> WE ARE NOT COUNTING VALID PARTITIONS, we are just returning 0 or 1

            #instead, we can LOOK to the next CHAR, considering the CURRENT COUPLE (i, i + 1) AS VALID, and go on
 

            if i < n - 1:
                if s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"):
                    res += dfs(i + 2) 

            return res

        return dfs(0)


#!O(N) time and space
#TOP-DOWN, memoization
#each character can be taken ALONE or WITH THE FOLLOWING CHARACTER
#this allows a SUMMING structure --> each CHAR can be VALID (1) or NOT VALID (0)
#going down to the RECURSION LEVELS we will see VALID PATHS made by 1 or 2 CHARS and we SUM THEM TOGETHER BACKWARDS
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo = [-1] * (n + 1)
        memo[n] = 1
        def dfs(i):
            if memo[i] != -1: #we finished the string --> valid
                return memo[i]
            
            if s[i] == "0": #we found a leading zero --> not valid
                return 0
            
            memo[i] = dfs(i + 1) #now that "i" is valid, we can consider the following character, this will add the current char as a valid char (inheriting the sum of next char)

            #EVALUATE COUPLE, without the following lines, we will just STOP at the first ZERO and return it (through ALL RECURSION LEVELS)
            #OR we would JUST RETURN 1 (if no zeros are found) --> WE ARE NOT COUNTING VALID PARTITIONS, we are just returning 0 or 1

            #instead, we can LOOK to the next CHAR, considering the CURRENT COUPLE (i, i + 1) AS VALID, and go on
 

            if i < n - 1:
                if s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"):
                    memo[i] += dfs(i + 2) 

            return memo[i]

        return dfs(0)


#!O(N) time and space
#BOTTOM-UP
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [-1] * (n + 1)
        dp[-1] = 1

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] if s[i] != "0" else 0
            if i < n - 1:
                if s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"):
                    dp[i] += dp[i + 2]
            

        return dp[0]

#!O(N) time and O(1) space
#BOTTOM-UP
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        curr = 1
        curr_c = None

        for i in range(n - 1, -1, -1):
            prev = curr if s[i] != "0" else 0
            if i < n - 1:
                if s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"):
                    prev += curr_c
            
            curr, curr_c = prev, curr
            

        return curr



        