
#!O(logN)
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if not n:
            return 1.0

        if n < 0:
            x = 1 / x
            n = - n

        currProd = x
        res = 1.0

        while n > 0:

            if n % 2 == 1:
                res *= currProd

            currProd *= currProd
            n //= 2
        
        return res