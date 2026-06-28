class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        nw1 = len(word1)
        nw2 = len(word2)
        
        p1, p2 = 0, 0
        
        while p1 < nw1 and p2 < nw2:
            res.append(word1[p1])
            res.append(word2[p2])

            p1 += 1
            p2 += 1
        
      
        res.append(word1[p1:]) 
        res.append(word2[p2:]) 
        
        return "".join(res)
        