
#!O(NlogN)
class Solution:
    

    def countBits(self, n: int) -> List[int]:
        res = []

        def countOnes(n):
            res = 0
            while n:
                n &= (n - 1)
                res += 1
            return res
            
        for num in range(n + 1):
            res.append(countOnes(num))
        
        return res

#!O(N)
#DP
#the number of ones in n are
#number of ones in highest power of two that is less than k (ALWAYS 1 SINCE)
# PLUS
#number of ones in the remainder (k - highest power of two)
class Solution:
    

    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        highestPower2 = 1

        for k in range(1, n + 1):
            if highestPower2 * 2 == k:
                highestPower2 = k
            
            dp[k] = 1 + dp[k - highestPower2]
        
        return dp

#!O(N)
#DP
#the number of ones in n are
#number of ones in n >> 1 
# PLUS
#1 if last bit is 1 else 0
class Solution:
    

    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for k in range(1, n + 1):
            dp[k] = dp[k >> 1] + (k & 1)
        
        return dp
        