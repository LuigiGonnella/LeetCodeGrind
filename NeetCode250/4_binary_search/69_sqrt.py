
#!O(logN)
class Solution:
    def mySqrt(self, x: int) -> int:
        res = -1
        l, r = 0, x + 1

        while l < r: 

            m = l + (r - l) // 2
            square = m * m
            
            if square == x:
                return m
            
            if square < x:
                l = m + 1
                res = m
            else:
                r = m
        
        return res
            
            

            
        