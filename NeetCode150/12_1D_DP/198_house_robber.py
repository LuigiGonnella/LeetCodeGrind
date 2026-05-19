
#!O(N) time and space
#TOP-DOWN, memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        if n <= 2:
            return max(nums)

        cache = [-1] * n
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])

        def dfs(i):
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])

            return cache[i]
        
        return dfs(n - 1)


#!O(N) time and space
#BOTTOM-UP
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n - 1]


#!O(N) time and O(1) space
#BOTTOM-UP
#since we only look i -1 and i - 2 (as climbing stairs problem), we don't need to store the ENTIRE array of length N
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        if n <= 2:
            return max(nums)

        prev_p = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(prev, prev_p + nums[i])
            prev_p, prev = prev, curr
        
        return curr
