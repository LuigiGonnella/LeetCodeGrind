
#!O(N) time and space
#TOP-DOWN, memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n <= 2:
            return max(nums)

        
        def dfs(i):
            nonlocal cache
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return cache[i]
        
        #CASE 1: START FROM 0
        cache = [-1] * n
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        
        res1 = dfs(n - 2)

        #CASE 2: START FROM 1
        cache = [-1] * n    
        cache[0] = 0
        cache[1] = nums[1]

        res2 = dfs(n - 1)
        
        return max(res1, res2)

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
        
        #CASE 1: START FROM 0
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        res1 = dp[n - 2]
        

        #CASE 2: START FROM 1
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])

        for i in range(3, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        res2 = dp[n - 1]
        
        return max(res1, res2)

#!O(N) time and O(1) space
#BOTTOM-UP
#since we only look i - 1 and i - 2 (as climbing stairs problem), we don't need to store the ENTIRE array of length N
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n <= 2:
            return max(nums)

        
        def rob_linear(start, end):
            prev, prev_p = 0, 0

            for i in range(start, end): #handles DP initialization aswell
                curr = max(prev, prev_p + nums[i])
                prev_p, prev = prev, curr
            
            return curr


        
        #CASE 1: START FROM 0
        # prev_p = nums[0]
        # prev = max(nums[0], nums[1])
        # curr = None

        # for i in range(2, n - 1):
        #     curr = max(prev, prev_p + nums[i])
        #     prev_p, prev = prev, curr
        
        # res1 = curr if curr else prev
        
        res1 = rob_linear(0, n - 1)

        #CASE 2: START FROM 1
        # prev_p = nums[1]
        # prev = max(nums[1], nums[2])
        # curr = None

        # for i in range(3, n):
        #     curr = max(prev, prev_p + nums[i])
        #     prev_p, prev = prev, curr

        # res2 = curr if curr else prev
        
        res2 = rob_linear(1, n)
        return max(res1, res2)


        


        