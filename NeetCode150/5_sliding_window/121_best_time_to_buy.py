class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[r] >= prices[l]:
                sP = prices[r] - prices[l]
                mP = max(mP, sP)
            else:
                l = r        
            
            r+=1
        
        return mP

#or

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#       minEl = prices[0]
        # maxProfit = 0

        # for price in prices:  
        #     maxProfit = max(price - minEl, maxProfit)
        #     minEl = min(minEl, price)
        
        # return maxProfit