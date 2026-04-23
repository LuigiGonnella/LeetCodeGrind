#O(N*M)
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False
#         occurrencies = [0] * 26

#         win_length = len(s1)

#         for i in range(len(s1)):
#             occurrencies[ord(s1[i]) - ord('a')] += 1

#         found = 1
#         for i in range(len(s2) - win_length + 1):
#             occ = occurrencies.copy()

#             for j in range(win_length):
#                 if occ[ord(s2[i+j]) - ord('a')] <= 0 and found:
#                     found = 0
#                 if found:
#                     occ[ord(s2[i+j]) - ord('a')] -= 1
            
#             if found:
#                 return True
            
#             found = 1

#         return False

#O(N)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        S1occ, S2occ = [0] * 26, [0] * 26

        for i in range(len(s1)):
            S1occ[ord(s1[i]) - ord('a')] += 1
            S2occ[ord(s2[i]) - ord('a')] += 1 #first window occurrencies

        matches = 0
        for j in range(26):
                matches += (1 if S1occ[j] == S2occ[j] else 0)
        
        l = 0
        print(f'initial matches: {matches}')
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')

            S2occ[index] += 1
            
            if S2occ[index] == S1occ[index]:
                matches += 1

            elif S2occ[index] - 1 == S1occ[index]:
                matches -= 1
            
            
            index = ord(s2[l]) - ord('a')

            S2occ[index] -= 1
            
            if S2occ[index] == S1occ[index]:
                matches += 1

            elif S2occ[index] + 1 == S1occ[index]:
                matches -= 1
            
            l += 1


        return matches == 26
    
#OR, SAME COMPLEXITY:
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s2) < len(s1):
#             return False

#         mapNeed = {}
#         mapHave = {}

#         for i in range(len(s1)):
#             mapNeed[s1[i]] = mapNeed.get(s1[i], 0) + 1
        
#         countTotCorrect = len(mapNeed)
#         countActCorrect = 0

#         for i in range(len(s1)):
#             if s2[i] not in mapNeed:
#                 continue
#             mapHave[s2[i]] = mapHave.get(s2[i], 0) + 1
#             if mapHave[s2[i]] == mapNeed[s2[i]]:
#                 countActCorrect += 1
        
#         l = 0
#         for r in range(len(s1), len(s2)):
#             if countActCorrect == countTotCorrect:
#                 return True
            
#             if s2[l] in mapNeed:
#                 mapHave[s2[l]] -= 1

#                 if mapHave[s2[l]] + 1 == mapNeed[s2[l]]:
#                     countActCorrect -= 1
            
#             if s2[r] in mapNeed:
#                 mapHave[s2[r]] = mapHave.get(s2[r], 0) + 1
#                 if mapHave[s2[r]] == mapNeed[s2[r]]:
#                     countActCorrect += 1
            
#             l += 1
        
#         return countActCorrect == countTotCorrect

        