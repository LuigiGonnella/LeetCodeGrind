
#!O(Bell number) --> too inefficient
#ER algorithm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k = 2
        res = []
        n = len(nums)

        def dfs(m):
            def isValid(subs):
                return sum(subs[0]) == sum(subs[1])
            
            def toArray(res):
                sub1 = []
                sub2 = []

                for i, sub in enumerate(res):
                    if sub == 0:
                        sub1.append(nums[i])
                    else:
                        sub2.append(nums[i])
                
                return [sub1, sub2]


            if len(res) == n:
                if m == k:
                    occ = set()
                    for sub in res:
                        occ.add(sub)
                    
                    subs = toArray(res)
                    
                    if len(occ) != m or not isValid(subs):
                        return False
                    
                    return True

                return False


            for i in range(m):
                res.append(i)

                if dfs(m):
                    return True

                res.pop()
            
            res.append(m)

            if dfs(m + 1):
                return True
            res.pop()

            return False

        
        return dfs(0)



#!O(2^N)
#odd sum --> impossible
#RECURSION
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        tot_sum = sum(nums)
        if tot_sum % 2:
            return False
        
        half_sum = tot_sum // 2
        n = len(nums)
        def dfs(i, target): #N runs

            if i == n:
                return target == 0
            
            if target < 0:
                return False
            
            
            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        return dfs(0, half_sum)


#!O(N * target) and O(N * target) space
#odd sum --> impossible
#TOP-DOWN
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        tot_sum = sum(nums)
        if tot_sum % 2:
            return False
        
        half_sum = tot_sum // 2
        n = len(nums)
        memo = {}
        def dfs(i, target): #N runs

            if i == n:
                return target == 0
            
            if target < 0:
                return False

            if (i, target) in memo:
                return memo[(i, target)]
            
            
            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i]) #for each, at most target reruns
            return memo[(i, target)]

        return dfs(0, half_sum)


#!O(N * target) and O(N * target) space
#odd sum --> impossible
#BOTTOM-UP --> classic knapsack solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot_sum = sum(nums)
        if tot_sum % 2:
            return False

        half_sum = tot_sum // 2

        n = len(nums)

        dp = [[False] * (n + 1) for _ in range(half_sum)]

        for i in range(1, n + 1):
            for j in range(half_sum):

                if half_sum - nums[i - 1] >= 0: #we can take it
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else: #we cannot take it
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][half_sum - 1]




#!O(N * target) and O(target) space
#odd sum --> impossible
#BOTTOM-UP

#at any time dp will have the TOTAL SUMS reachable with the processed numbers
#if it will ever contain target --> return True
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot_sum = sum(nums)
        if tot_sum % 2:
            return False

        half_sum = tot_sum // 2

        n = len(nums)
        dp = set()
        dp.add(0) #at the begin no number is processed


        for i in range(n): #at the end of the first iteration --> dp will contain every single sum (single elements)
        #then every single + couple sums, then every single + couple  + triplet, and so on
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == half_sum:
                    return True
                
                nextDP.add(t + nums[i])
                nextDP.add(t)
            
            dp = nextDP
            
        
        return False








        
        