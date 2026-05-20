
#!O(N^2) time and space
#DP
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        res = 0

        for i in range(n - 1, -1 , -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i <= 2) or dp[i + 1][j - 1] == True):
                    dp[i][j] = True
                    res += 1
        return res


#!O(N^2) time and O(1) space
#TWO POINTERS
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def countPal(l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            return res
    
        res = 0
        for i in range(n):
            res += countPal(i, i) #ODD case
            res += countPal(i, i + 1) #EVEN case (if i out of boundary it will return immediately)

        return res
        