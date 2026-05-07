# O(2 ^ N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        res = []

        def isPalindrome(curr):
            l = 0
            r = len(curr) - 1

            while l <= r:
                if curr[l] != curr[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        def dfs(i):

            if i >= len(s):
                res.append(part.copy())
                return


            for j in range(i, len(s)):
                if isPalindrome(s[i : j + 1]):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

