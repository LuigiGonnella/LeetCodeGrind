
#!O(1) time and space
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483648
        MIN = -2147483648

        multiplier = 1

        digits = list(str(x)[::-1])
        res = 0

        negative = 1
        if digits[-1] == "-":
            negative = -1
            digits.pop()
        
        while digits:
            digit = int(digits.pop())

            if digit > MAX // multiplier or (digit == MAX // multiplier and res > MAX % multiplier):
                return 0
            
            res += (digit * multiplier)
            multiplier *= 10
        
        return res * negative