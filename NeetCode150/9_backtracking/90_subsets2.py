
#!POWERSET DISP. RIP + TUPLE TO AVOID DUPLICATES
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr_sol = []
        

        def dfs(i: int) -> None:

            if i == len(nums):
                res.add(tuple(curr_sol))
                return

            curr_sol.append(nums[i])
            dfs(i + 1)

            curr_sol.pop()
            dfs(i + 1)
        
        nums.sort()
        dfs(0)
        return [list(s) for s in res]


#!POWERSET DISP. RIP. + SORT TO AVOID DUPLICATES
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:  
        nums.sort()
        res = []
        curr_sol = []

        def dfs(i: int):
            if i == len(nums):
                res.append(curr_sol.copy())
                return
            

            curr_sol.append(nums[i])
            dfs(i + 1)

            curr_sol.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: #skip as first element of subset if already considered
                i += 1

            
            dfs(i + 1)
        
        dfs(0)

        return res

#!POWERSET COMB. SEMPL. + SORT TO AVOID DUPLICATES
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        def dfs(start: int) -> None:

            #at every call i will have a new subset
            res.append(subset.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
            
        dfs(0)
        return res
