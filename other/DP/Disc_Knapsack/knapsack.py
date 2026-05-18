
#!O(Nitems * CAP)
#only max value
class Solution:

    # class Item:
    #     def __init__(self, w = 0, val = 0):
    #!         self.w = w #WEIGHT
    #!         self.val = val #VALUE

    def knapsack(self, cap, items):
        n = len(items)
        dp = [[0] * (cap + 1) for _ in range(n + 1)] #MATRIX where ROW = HOW MANY ITEMS I SAW UNTIL NOW and COL = MAX CAPACITY CONSIDERED UNTIL NOW

        for i in range(1, n + 1): #considering AN ITEM AT THE TIME
            for j in range(1, cap + 1): #FOR EACH POSSIBLE CAPACITY
                if items[i - 1].w > j: #IF THE ITEM DOESN'T FIT (CANNOT TAKE IT)
                    dp[i][j] = dp[i - 1][j] #MAINTAIN THE VALUE OF THE SPACE WHERE I SAW UNTIL LAST ITEM, WITH THE SAME AVAILABE CAPACITY
                else: #ITEM FITS
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1].w] + items[i - 1].val) #TAKE IT ONLY IF GOING BACK TO THE VALUE WHERE CAPACITY WAS SMALL ENOUGH 
                    #TO CONTAIN THIS NEW ITEM + NEW VALUE IS BIGGER THAN NOT TAKING IT (CONSIDERING VALUE WITHOUT TAKING IT, SAME AS BEFORE)
        
        return dp[n][cap] #RETURN BEST VAL WHEN I SAW EVERY ITEM, COSNIDERING MEVERY CAPACITY (up to max cap)



#!O(CAP)
#only max value
class Solution:
    def knapsack(self, cap, items):
        n = len(items)
        # We only need a 1D array of size (cap + 1)
        dp = [0] * (cap + 1)
        
        for i in range(n):
            # Iterate backwards through capacities! 
            # This ensures we don't use the same item multiple times.
            for j in range(cap, (items[i].w - 1), -1):
                dp[j] = max(dp[j], dp[j - items[i].w] + items[i].val)
                
        return dp[cap]

#!O(Nitems * CAP)
#items reconstruction
class Solution:

    # class Item:
    #     def __init__(self, w = 0, val = 0):
    #!         self.w = w #WEIGHT
    #!         self.val = val #VALUE

    def knapsack(self, cap, items):
        n = len(items)
        dp = [[0] * (cap + 1) for _ in range(n + 1)] #MATRIX where ROW = HOW MANY ITEMS I SAW UNTIL NOW and COL = MAX CAPACITY CONSIDERED UNTIL NOW

        for i in range(1, n + 1): #considering AN ITEM AT THE TIME
            for j in range(1, cap + 1): #FOR EACH POSSIBLE CAPACITY
                if items[i].w > j: #IF THE ITEM DOESN'T FIT (CANNOT TAKE IT)
                    dp[i][j] = dp[i - 1][j] #MAINTAIN THE VALUE OF THE SPACE WHERE I SAW UNTIL LAST ITEM, WITH THE SAME AVAILABE CAPACITY
                else: #ITEM FITS
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i].w] + items[i].val) #TAKE IT ONLY IF GOING BACK TO THE VALUE WHERE CAPACITY WAS SMALL ENOUGH 
                    #TO CONTAIN THIS NEW ITEM + NEW VALUE IS BIGGER THAN NOT TAKING IT (CONSIDERING VALUE WITHOUT TAKING IT, SAME AS BEFORE)
        
        res = []

        i, j = n, cap
        while i > 0 and j > 0:
            if dp[i][j] > dp[i - 1][j]: #taken
                res.append(items[i - 1])
                j -= items[i - 1].w
            
            #not taken --> cap is the same                
            
            i -= 1 #always go to next item
            
        
        return res, dp[n][cap] #RETURN ITEMS +  BEST VAL WHEN I SAW EVERY ITEM, COSNIDERING MEVERY CAPACITY (up to max cap)
