
#!O(2^N) time and O(N) space
#RECURSION
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        def dfs(i, have_coin):

            if i >= n:
                return 0

            if have_coin: # i can sell
                return max(dfs(i + 2, False) + prices[i], dfs(i + 1, True)) #max between selling and goind 2 days ahead or not selling and going next day
            
            #i cannot sell, but i can buy (constraint of buy only 24h after last sell is naturally handled buy recursion in "have_coin" branch)
            return max(dfs(i + 1, False), dfs(i + 1, True) - prices[i]) #max between buy and not buy
        
        return dfs(0, False)

#!O(N) time and space
#TOP-DOWN, memoization            
class Solution: #0 = False, 1 = True
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        memo = [[-1] * n for _ in range(2)]
        def dfs(i, have_coin):

            if i >= n:
                return 0
            
            if memo[have_coin][i] != -1 :
                return memo[have_coin][i]

            if have_coin: # i can sell
                memo[have_coin][i]= max(dfs(i + 2, 0) + prices[i], dfs(i + 1, 1)) #max between selling and goind 2 days ahead or not selling and going next day
                return memo[have_coin][i]
            
            #i cannot sell, but i can buy
            memo[have_coin][i] = max(dfs(i + 1, 0), dfs(i + 1, 1) - prices[i]) #max between buy and not buy
            return memo[have_coin][i] 
        
        return dfs(0, 0)
            

#!O(N) time and space
# #BOTTOM-UP            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices) 
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for have_coin in [True, False]:
                if have_coin: #i can sell
                    amount_with_sell = dp[i + 2][False] + prices[i] if i + 2 < n else prices[i] #I sell coming from not having the coin two days before
                    amount_without_sell = dp[i + 1][True] if i + 1 < n else 0 #I skip, maintain previous amounr having the coin
                    dp[i][True] = max(amount_with_sell, amount_without_sell) #Store maximum having the coin
                else: #I can buy, but only if i didn't sell previous day
                    amount_with_buy = dp[i + 1][True] - prices[i] if i + 1 < n else -prices[i] #I buy coming from having the coin
                    amount_without_buy = dp[i + 1][False] if i + 1 < n else 0 #I skip coming from not having the coin (meaning i cannot buy)
                    dp[i][False] = max(amount_with_buy, amount_without_buy) #Store maximum not having the coin
        
        return dp[0][0] #maximum not having the coin first day










        