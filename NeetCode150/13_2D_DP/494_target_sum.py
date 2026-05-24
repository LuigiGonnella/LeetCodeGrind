
#!O(2 ^ N) time and O(N) space
#RECURSION
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        def dfs(i, curr_sum):

            if i == n and curr_sum == target:
                return 1
            
            if i == n:
                return 0
            

            res = dfs(i + 1, curr_sum - nums[i]) #subtract
            res += dfs(i + 1, curr_sum + nums[i]) #add

            return res
        
        return dfs(0, 0)


#!O(N*sum(nums)) time and space 
#MEMOIZATION
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        memo = {}

        def dfs(i, curr_sum):

            if i == n and curr_sum == target:
                return 1
            
            if i == n:
                return 0
            
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            
            res = dfs(i + 1, curr_sum - nums[i])
            res += dfs(i + 1, curr_sum + nums[i])
            memo[(i, curr_sum)] = res
            return res
        
        return dfs(0, 0)


#!O(N*sum(nums)) time and space 
#BOTTOM-UP 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(n):
            for curr_sum, count in dp[i].items():
                dp[i + 1][curr_sum - nums[i]] += count
                dp[i + 1][curr_sum + nums[i]] += count
        
        return dp[n][target]


#!O(N*sum(nums)) time and O(sum(nums)) space --> each step depends only on the previous step!
#BOTTOM-UP 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int) 

        dp[0] = 1

        for i in range(n):
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum - nums[i]] += count
                next_dp[curr_sum + nums[i]] += count
            dp = next_dp
        
        return dp[target]










        