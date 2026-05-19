
#!O(N^3)
#BRUTE FORCE

#!O(N^2) time and space
#BOTTOM-UP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)] #dp[i][j] True if s[i:j] is palindrome       
        resIdx, resLen = 0, 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i) <= 2 or dp[i + 1][j - 1]): #if equal chars and inner string is palindromic (or the actual len is < 3, so no inner string to check) --> this substring IS PALINDOMIC
                    dp[i][j] = True

                    if (j - i + 1) > resLen:
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx: resIdx + resLen]

#!O(N^2) time and O(1) space
#TWO POINTERS
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resIdx, resLen = 0, 0

        #we expand from center as much as we can, from every INDEX cosnidered as center
        
        #ODD LENGTH --> center is a single character
        for i in range(n):
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:

                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                
                l -= 1
                r += 1
        
        #EVEN LENGTH --> center is two characters
        for i in range(n):
            l, r = i, i + 1

            while l >= 0 and r < n and s[l] == s[r]:

                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                
                l -= 1
                r += 1
        
        return s[resIdx: resIdx + resLen]
        