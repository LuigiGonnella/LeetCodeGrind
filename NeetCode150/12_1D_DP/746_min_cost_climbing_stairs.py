# #!O(N) time and space
# #BOTTOM-UP
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) <= 2:
            return min(cost)

        n = len(cost) + 1
        dp = [0] * n 

        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n - 1]

#!O(N) time and space
#TOP-DOWN
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        n = len(cost) + 1
        cache = [-1] * n
        cache[0], cache[1] = 0, 0 

        
        def dfs(i):
            if cache[i] != -1:
                return cache[i]

            cache[i] = min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
            return cache[i]
        
        
        return dfs(n - 1)

#!O(N) time and O(1) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2]) 
            #to overlap FROM cost[i] I can do:
            #!1 STEP (PAY cost[i] + cost[i + 1]) + 2 STEP (overlap = cost free) OR
            #!2 STEPS (PAY cost[i] + cost[i + 2]) + 2 STEP (overlap = cost free)
        
        
        return min(cost[0], cost[1])
        