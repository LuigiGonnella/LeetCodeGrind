
#!O(N ^ AMOUNT) time and space
# class Solution:
def coinChange(self, coins: List[int], amount: int) -> int:

    def dfs(amount):
        if not amount:
            return 0
        

        res = float("+inf")

        for coin in coins: #every coin looks at every other coin AMOUNT times (max)
            if amount - coin >= 0:
                res = min(res, 1 + dfs(amount - coin))
            
        return res

    minC = dfs(amount)
    return minC if minC != float("+inf") else -1


#!O(N * AMOUNT) and O(AMOUNT) space
#TOP-DOWN, memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        memo[0] = 0

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            
            res = float("+inf")
            for coin in coins: #for every AMOUNT times we loop over all coins
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= float("+inf") else minCoins

#!O(N * AMOUNT) time and O(AMOUNT) space
#BOTTOM-UP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for am in range(1, amount + 1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am], 1 + dp[am - coin])
        
        return dp[amount] if dp[amount] < (amount + 1) else -1


























            