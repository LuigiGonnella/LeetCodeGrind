
#!O(N) tiem and space
#BOTTOM-UP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]


# !O(N) time and space
# MEMOIZATION (TOP-DOWN)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        cache = [0] * (n + 1)
        cache[1], cache[2] = 1, 2

        def dfs(i):
            if cache[i]:
                return cache[i]

            cache[i] = dfs(i - 1) + dfs(i - 2)
            return cache[i]
        
        return dfs(n)

#!O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        # a is step (i-2), b is step (i-1)
        a, b = 1, 2
        
        # Start calculating from step 3 up to n
        for _ in range(3, n + 1):
            # The new step is the sum of the last two. 
            # Then shift the variables forward.
            a, b = b, a + b
            
        return b