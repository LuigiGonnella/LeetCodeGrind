
#RECURSION
#!O(N * 2^N) time and O(2N) space
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)

        nums_b = [1] + nums + [1]

        #divide and conquer --> given a range i find the mximum product bursting all baloons inside this range
        #trying for every baloon in the range to be the last to be bursted
        #so the single partial sol (for each i in range) is dfs(l, i) * nums[i] * dfs(i, r)
        def dfs(l, r): #l and r exluded 

            if l >= r - 1: #no baloons in the range
                return 0
            
            
            maxRes = -1
            for i in range(l + 1, r):
                curr_sol = nums_b[l] * nums_b[i] * nums_b[r] #pop i as LAST
                curr_sol += (dfs(l, i) + dfs(i, r)) #pop all other ones
                maxRes = max(maxRes, curr_sol)
            
            return maxRes

        return dfs(0, n + 1)


#!O(N^3) time and O(N^2) space
#TOP-DOWN, memoization
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)

        nums_b = [1] + nums + [1]
        memo = [[-1] * (n + 2) for _ in range(n + 2)]

        #divide and conquer --> given a range i find the mximum product bursting all baloons inside this range
        #trying for every baloon in the range to be the last to be bursted
        #so the single partial sol (for each i in range) is dfs(l, i) * nums[i] * dfs(i, r)
        def dfs(l, r): #l and r exluded 

            if l >= r - 1: #no baloons in the range
                return 0
            
            if memo[l][r] != -1:
                return memo[l][r]
            
            
            maxRes = -1
            for i in range(l + 1, r):
                curr_sol = nums_b[l] * nums_b[i] * nums_b[r] #pop i as LAST
                curr_sol += (dfs(l, i) + dfs(i, r)) #pop all other ones
                maxRes = max(maxRes, curr_sol)

            memo[l][r] = maxRes
            
            return maxRes

        return dfs(0, n + 1)


#!O(N^3) time and O(N^2) space
#BOTTOM UP
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)

        nums_b = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]


        #divide and conquer --> given a range i find the mximum product bursting all baloons inside this range
        #trying for every baloon in the range to be the last to be bursted
        #so the single partial sol (for each i in range) is dfs(l, i) * nums[i] * dfs(i, r)
        
        for i in range(n - 1, -1, -1): #l
            for j in range(i + 2, n + 2): #r
                for k in range(i + 1, j):
                    res = nums_b[i] * nums_b[k] * nums_b[j]
                    dp[i][j] = max(res + dp[i][k] + dp[k][j], dp[i][j])
        
        return dp[0][n + 1]

        