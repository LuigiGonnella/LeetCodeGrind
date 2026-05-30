
#!O(2^N) time and O(N) space
#BRUTE FORCE
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        if not triplets:
            return False

        n = len(triplets)

        def dfs(curr_triplet, i):
            if curr_triplet == target:
                return True
            
            if i == n:
                return False
            
            #don't take it
            if dfs(curr_triplet, i + 1):
                return True
            
            #take it
            curr_triplet = [max(tr1, tr2) for tr1, tr2 in zip(curr_triplet, triplets[i])]
            if dfs(curr_triplet, i + 1):
                return True
            
            return False
        
        return dfs([float("-inf"), float("-inf"), float("-inf")], 0)
            

#!O(N^4) time and space --> N "i", N idx = 0, N idx = 1 and N idx = 2
#MEMOIZATION
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        if not triplets:
            return False

        n = len(triplets)
        memo = {}

        def dfs(curr_triplet, i):
            if curr_triplet == target:
                return True
            
            if i == n:
                return False
            
            if (tuple(curr_triplet), i) in memo:
                return memo[(tuple(curr_triplet), i)]

            #don't take it
            if dfs(curr_triplet, i + 1):
                memo[(tuple(curr_triplet), i)] = True
                return True
            
            #take it
            curr_triplet = [max(tr1, tr2) for tr1, tr2 in zip(curr_triplet, triplets[i])]
            if dfs(curr_triplet, i + 1):
                memo[(tuple(curr_triplet), i)] = True
                return True
            
            memo[(tuple(curr_triplet), i)] = False
            return False
        
        return dfs([float("-inf"), float("-inf"), float("-inf")], 0)   

#!O(N) time and O(1) space
#GREEDY
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        have = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i, v in enumerate(triplet):
                if v == target[i]:
                    have.add(i)
            
            if len(have) == 3:
                return True

        return False

#!O(N) time and O(1) space
#GREEDY
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        x = y = z = False

        for triplet in triplets:
            x |= triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]
            y |= triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]
            z |= triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]

            if x and y and z:
                return True

        return False
