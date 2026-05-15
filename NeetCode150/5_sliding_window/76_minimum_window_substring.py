#time O(N) and space O(M)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countHave = {}
        countNeed = {}

        correctHave = 0

        for i in range(len(t)):
            countNeed[t[i]] = countNeed.get(t[i], 0) + 1
        
        correctNeed = len(countNeed)

        l, r = 0, 0
        
        bestLen = float("+inf")
        bestSub = ""

        for r in range(len(s)):
            if s[r] not in countNeed:
                continue
            
            countHave[s[r]] = countHave.get(s[r], 0) + 1

            if countHave[s[r]] == countNeed[s[r]]:
                correctHave += 1

            while correctHave == correctNeed:
                if r - l + 1 < bestLen:
                    bestLen = r - l + 1
                    bestSub = s[l:r + 1]
                
                if s[l] in countHave:
                    countHave[s[l]] -= 1
                    
                if s[l] in countNeed and countHave[s[l]] < countNeed[s[l]]:
                    correctHave -= 1
                
                l += 1
            
        
        return bestSub



        