
#O(n + m)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        if str1 + str2 != str2 + str1:
            return ""
        
        while m != 0:
            n, m = m, n % m
        
        return str1[:n]
