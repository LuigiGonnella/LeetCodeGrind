

#RECURSION
#!O(2^N) and O(N) space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)

        def dfs(i):

            if i == n - 1:
                return True
            
            if not nums[i]:
                return False

            
            res = False
            jump = 1

            while not res and jump <= nums[i]:
                res = res or dfs(i + jump)
                jump += 1
            
            return res
        
        return dfs(0)


#RECURSION, memoization
#!O(N ^ 2) time and O(N) space --> for each state we check possibly every other state
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        memo = [-1] * (n - 1)

        def dfs(i):

            if i == n - 1:
                return True
            
            if not nums[i]:
                return False
            
            if memo[i] != -1:
                return memo[i]

            
            res = False
            jump = 1

            while not res and jump <= nums[i]:
                res = res or dfs(i + jump)
                jump += 1
            
            memo[i] = res
            return res
        
        return dfs(0)

#BOTTOM-UP
#!O(N ^ 2) time and O(N) space --> for each state we check possibly every other state
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        dp = [False] * n 
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            jump = 1

            while not dp[i] and jump <= nums[i]:
                dp[i] = dp[i] or dp[i + jump]
                jump += 1
        
        return dp[0]


#!O(N) time and O(1) space
#GREEDY
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        target = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= target: #if we can reach target from i --> i becomes new target
                target = i
        
        return target == 0












