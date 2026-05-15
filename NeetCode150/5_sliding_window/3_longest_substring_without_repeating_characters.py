class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        uniques = {}
        while r < len(s):
            if s[r] in uniques:
                maxLen = max(r - l, maxLen)
                l = max(uniques[s[r]] + 1, l)
            
            uniques[s[r]] = r
            r+=1
        
        maxLen = max(r - l, maxLen)
        return maxLen
            

            



        