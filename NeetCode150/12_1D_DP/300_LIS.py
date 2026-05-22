
#!O(2^N) time and O(N) space
#BACKTRACK
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curr = []
        maxL = -1
        n = len(nums)

        def dfs(i):
            nonlocal maxL
            def isValid(curr):
                n = len(curr)
                for i in range(1, n):
                    if curr[i] <= curr[i - 1]:
                        return False
                return True



            if i == n:
                if isValid(curr):
                    maxL = max(maxL, len(curr))
                return
            

            curr.append(nums[i])
            dfs(i + 1)
            curr.pop() #bactrack
            dfs(i + 1)
        
        dfs(0)
        return maxL
                



#!O(N^2) time and O(N^2) space
#MEMOIZATION
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(prev, curr):
            if curr == n:
                return 0
            
            if (prev, curr) in memo:
                return memo[(prev, curr)]
            

            maxL = dfs(prev, curr + 1) #not_take

            if prev == -1 or nums[curr] > nums[prev]:
                take = 1 + dfs(curr, curr + 1)
                maxL = max(maxL, take)

            memo[(prev, curr)] = maxL
            return maxL
        
        
        return dfs(-1, 0)



#!O(N^2) time and O(N) space
#BOTTOM-UP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1

        for i in range(1, n):
            for j in range(i + 1):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    res = max(res, dp[i])
        
        return res

#!O(NlogN) time and O(N) space
#BOTTOM-UP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = []
        
        for num in nums:

            if not sub or num > sub[-1]:
                sub.append(num)
                continue
            
            l, r = 0, len(sub) - 1
            pos = None
            
            while l <= r:
                m = l + (r - l) // 2

                if num > sub[m]:
                    l = m + 1
                else:
                    pos = m
                    r = m - 1
            
            sub[pos] = num
            
        
        return len(sub)       






