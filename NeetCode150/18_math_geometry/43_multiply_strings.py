
#! O(N) time and space
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def convertToNum(s: str) -> int:
            multiplier = 10
            num = int(s[0])

            for i in range(1, len(s)):
                num *= multiplier
                num += int(s[i])
            
            return num
        
        num1_int = convertToNum(num1)
        num2_int = convertToNum(num2)

        return str(num1_int * num2_int)

        # def convertToString(num: int) -> str:
        #     if not num:
        #         return "0"
            
        #     string = []

        #     while num > 0:
        #         string.append(str(num % 10))
        #         num //= 10
            
        #     return "".join(reversed(string))
        
        #return convertToString(res)

        