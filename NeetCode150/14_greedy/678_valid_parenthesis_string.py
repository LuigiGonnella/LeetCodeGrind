
#!O(3^N) time and O(N) space
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        def dfs(i, opens):
            if opens < 0:
                return False

            if i == n:
                return opens == 0
                        
            if s[i] == "(":
                return dfs(i + 1, opens + 1)
            
            if s[i] == ")":
                return dfs(i + 1, opens - 1)
            
            return dfs(i + 1, opens - 1) or dfs(i + 1, opens + 1) or dfs(i + 1, opens) #treat star as open, closed of empty
        
        return dfs(0, 0)


#!O(N^2) time and space
#MEMOIZATION
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        def dfs(i, opens):
            if opens < 0:
                return False

            if i == n:
                return opens == 0
            
            if memo[i][opens] != -1:
                return memo[i][opens]
                        
            if s[i] == "(":
                res = dfs(i + 1, opens + 1)
            elif s[i] == ")":
                res = dfs(i + 1, opens - 1)
            else:
                res = dfs(i + 1, opens - 1) or dfs(i + 1, opens + 1) or dfs(i + 1, opens) #treat star as open, closed of empty
            
            memo[i][opens] = res
            return res
        
        return dfs(0, 0)

#!O(N^2) time and space
#BOTTOM-UP
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True #finished the string with 0 open left

        for i in range(n - 1, -1, -1):
            for open in range(n):
                res = False
                if s[i] == '*':
                    res |= dp[i + 1][open + 1]
                    if open > 0:
                        res |= dp[i + 1][open - 1]
                    res |= dp[i + 1][open]
                else:
                    if s[i] == '(':
                        res |= dp[i + 1][open + 1]
                    elif open > 0:
                        res |= dp[i + 1][open - 1]
                dp[i][open] = res 


        return dp[0][0]

#!O(N^2) time and O(N) space
#BOTTOM-UP
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        
        next_dp = [False] * (n + 1)
        next_dp[0] = True

        for i in range(n - 1, -1, -1):   
            dp = [False] * (n + 1)              
            for open in range(n):
                res = False
                if s[i] == '*':
                    res |= next_dp[open + 1]
                    if open > 0:
                        res |= next_dp[open - 1]
                    res |= next_dp[open]
                else:
                    if s[i] == '(':
                        res |= next_dp[open + 1]
                    elif open > 0:
                        res |= next_dp[open - 1]
                dp[open] = res 
            
            next_dp = dp


        return next_dp[0]

#!O(N) time and space
class Solution:
    def checkValidString(self, s: str) -> bool:

        open_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == ")": #we must pop
                if open_stack: #if ther is an open par. available, pop it
                    open_stack.pop()
                elif star_stack: #otherwise pop a star, treating it like an open par.
                    star_stack.pop()    
                else: #if none is available --> False
                    return False
            elif char == "(":
                open_stack.append(i)
            elif char == "*":
                star_stack.append(i)
        
        if len(star_stack) >= len(open_stack): #if we can close all open

            while open_stack: #see if all stars can close all the open (if they have a bigger index than open)
                i = star_stack.pop()
                j = open_stack.pop()

                if j > i: #if open is after the last start --> cannot close it
                    return False
        
        else: #if more open than star --> we cannot close all the remaining open --> False
            return False
        
        return True

#!O(N) time and O(1) space
class Solution:
    def checkValidString(self, s: str) -> bool:

        minLeft = 0 #min possible left par
        maxLeft = 0 #max possible left par

        for char in s:
            if char == "(":
                minLeft, maxLeft = minLeft + 1, maxLeft + 1 #increase both --> we found (
            elif char == ")":
                minLeft, maxLeft = minLeft - 1, maxLeft - 1 #decrease both --> we found )                
            else:
                minLeft, maxLeft = minLeft - 1, maxLeft + 1 #if ) increase nimLeft, if ( increase maxLeft
            
            if maxLeft < 0: #went negative --> more ) than ( "( + *" )
                return False
            
            if minLeft < 0: #we clear minLeft trating the exceeding * as empty
                minLeft = 0
        
        return minLeft == 0 #we want minLeft to be 0 at then end, otherwise it means that we had * before (


        