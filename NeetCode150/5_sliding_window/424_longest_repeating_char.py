class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occ_map = defaultdict(int)
        l = 0
        maxLen = 0
        maxFreq = 0

        for r in range(len(s)):
            occ_map[s[r]]+=1
            maxFreq = max(maxFreq, occ_map[s[r]])
            
            while (r - l + 1) - maxFreq > k:
                occ_map[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
                
        return maxLen

#O(N) time
#O(M) space with M = number of unique characters in string (number of keys in hash map)