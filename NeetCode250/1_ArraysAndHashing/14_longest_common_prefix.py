
#!O(N * M) where N = prefix length and M = number of words
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        idx = 0
        n = len(strs)
        while True:
            for i in range(n - 1):
                if (idx < len(strs[i]) and idx < len(strs[i + 1]) and strs[i][idx] != strs[i + 1][idx]) or idx >= len(strs[i]) or idx >= len(strs[i + 1]):
                    return res 
                
            if idx < len(strs[0]):
                res += strs[0][idx]
            else:
                return res

            idx += 1