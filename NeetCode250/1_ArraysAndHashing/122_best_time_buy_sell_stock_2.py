class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        buy = 0

        for sell in range(len(prices)):
            if prices[sell] > prices[buy]:
                tot += (prices[sell] - prices[buy])
            
            buy = sell
        
        return tot
        