
#!O(n_words ^ 2 * len(word) ^ 2 )
class Solution:
    def solve(words):

        final_res = []

        for reference in words: #word to break
            n = len(reference)
            dp = [False] * (n + 1) #dp[i] says if from i to n we can match the reference
            dp[n] = True
            for i in range(n - 1, -1, -1):
                for word in words:
                    if word != reference:
                        l = len(word)
                        if reference[i: i + l] == word:
                            dp[i] = dp[i + l]

                            if dp[i]:
                                break
            #If dp[0] is valid, walk forward along the verified path
            if dp[0]:
                res = []
                idx = 0
                while idx < n:
                    for word in words:
                        if word != reference:
                            l = len(word)
                            # The word must match AND the landing index must remain valid
                            if reference[idx: idx + l] == word and dp[idx + l]:
                                res.append(word)
                                idx += l
                                break
                final_res.append(res)
            
        return final_res

                 
                        
