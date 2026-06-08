class Solution:
    def solve(x, n) -> float: # we want pow(x, n)

        if not n:
            return 1.0

        if n < 0: #handle negatives
            x = 1 / x #reciprocal
            n = - n
        
        res = 1.0
        curr_prod = x

        while n > 0:

            if n % 2 == 1: #odd
                res *= curr_prod
            
            curr_prod *= curr_prod
            n //= 2
        
        return res