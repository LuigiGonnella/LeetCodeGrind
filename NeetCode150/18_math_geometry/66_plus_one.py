
#!O(N) time and O(1) extra-space
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) 
        res = [-1] * n
        
        rem = 0

        for i in range(n - 1, -1, -1):
            digit = digits[i]

            if i == n - 1:
                res_digit = digit + 1 + rem
            else:
                res_digit = digit + rem
            
            rem = res_digit // 10
            res_digit %= 10

            res[i] = res_digit
        
        if rem:
            res = [rem] + res

        
        return res

        