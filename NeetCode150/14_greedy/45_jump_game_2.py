
#RECURSION
#!O(N!) time and O(N) space
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i):
            if i == n - 1:
                return 0
            
            if i >= n:
                return float("inf")

            
            steps = float("inf")

            for j in range(1, nums[i] + 1):
                steps = min(steps, 1 + dfs(i + j))
            
            return steps
        
        return dfs(0)



#TOP-DOWN, memoization
#!O(N ^ 2) time and O(N) space
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [-1] * n

        def dfs(i):
            if i == n - 1:
                return 0
            
            if i >= n:
                return float("inf")
            
            if memo[i] != -1:
                return memo[i]

            
            steps = float("inf")

            for j in range(1, nums[i] + 1):
                steps = min(steps, 1 + dfs(i + j))
            
            memo[i] = steps
            return steps
        
        return dfs(0)      

#BOTTOM-UP
#!O(N ^ 2) time and O(N) space
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [float("+inf")] * n #dp[i] contains the min number of jumps from i to reach n - 1

        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i] = min(dp[i], 1 + dp[i + j]) #min between (current min) and (jump + min of the destination)
        
        return dp[0]



#GREEDY --> BFS of all reachable nodes starting from 0
#all reachable nodes (current level) are stored in a window [l, r] instead of a queue, but the idea is the same of a BFS (tells us the minimum number of edges to reach a target)
#!O(N) time and O(1) space
class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        l = r = 0
        
        steps = 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1 
            r = farthest
            steps += 1
        
        return steps
                


            
                





