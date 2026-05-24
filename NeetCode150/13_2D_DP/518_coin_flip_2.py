#BRUTE FORCE SOLUTION --> try every combination --> inefficient
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         res = 0

#         def dfs(start, curr_amount):
#             nonlocal res

#             if not curr_amount:
#                 res += 1
#                 return

#             for i in range(start, n):
#                 coin = coins[i]
#                 if amount - coin >= 0: 
#                     dfs(i, amount - coin)

#         dfs(0, amount)
#         return res


#!BAD SOLUTION --> DUPLICATE SOLUTIONS (combinaz. con rip.) --> serve controllo sull'indice

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)


#         def dfs(curr_amount):

#             if not curr_amount:
#                 return 1

#             res = 0

#             for i in range(n):
#                 coin = coins[i]
#                 if curr_amount - coin >= 0: 
#                     res += dfs(curr_amount - coins[i])
            
#             return res
        
#         return dfs(amount)


#!2^(max(M, N)) time and O(max(M, N)) space with M=amount and N =len(coins)
#RECURSION --> problema delle ripetizioni gestita nativamente dal fatto che non guardiamo mai indietro, ma solo avanti (tak/dont take)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)


        def dfs(i, curr_amount): #2^(max(M, N) with M=amount and N =len(coins)

            if not curr_amount:
                return 1

            if i >= n:
                return 0
            
        
            res = 0

            coin = coins[i]
            res += dfs(i + 1, curr_amount) #don't take
            if curr_amount - coin >= 0: #if i can take it
                res += dfs(i, curr_amount - coin) #take
                

            
            return res
        
        return dfs(0, amount)


#!(M * N) time and space with M=amount and N =len(coins)
#MEMOIZATION
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1] * n for _ in range(amount + 1)]

        def dfs(i, curr_amount): #2^(max(M, N) with M=amount and N =len(coins)

            if not curr_amount:
                return 1

            if i >= n:
                return 0

            if memo[curr_amount][i] != -1:
                return memo[curr_amount][i]
        
            res = 0
            coin = coins[i]

            res += dfs(i + 1, curr_amount) #don't take
            if curr_amount - coin >= 0: #if i can take it
                res += dfs(i, curr_amount - coin) #take
            

            memo[curr_amount][i] = res
            return res
        
        return dfs(0, amount)

#!(M * N) time and space with M=amount and N =len(coins)
#BOTTOM-UP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        #stores how many combinations including coins[i] can be chosen to form j = amount
        dp = [[0] * (amount + 1) for _ in range(n + 1)] #coins x amounts

        for i in range(n + 1):
            dp[i][0] = 1 #when amount = 0 --> only one way to have it (no coins)

        for i in range(1, n + 1): #for each coin
            coin = coins[i - 1]
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j] #don't take it --> inherit combinations until previous coin

                if j >= coin: #if i can take it
                    dp[i][j] += dp[i][j - coin] #take it --> add combinations obtained with previous amount 
        
        return dp[n][amount]

#!(M * N) time and O(M) space with M=amount and N =len(coins)
#BOTTOM-UP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        #stores how many combinations including coins[i] can be chosen to form j = amount

        curr_row = [0] * (amount + 1)
        curr_row[0] = 1


        for i in range(1, n + 1): #for each coin
            coin = coins[i - 1]
            for j in range(coin, amount + 1): #if i can take it
                curr_row[j] += curr_row[j - coin] #take it --> add combinations obtained with previous amount 
            
        
        return curr_row[amount]













