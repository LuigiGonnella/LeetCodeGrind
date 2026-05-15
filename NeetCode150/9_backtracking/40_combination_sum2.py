class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        curr_sol = []
        candidates.sort() #sort array to handle DUPLICATES and PRUNING

        def dfs(start: int, curr_sum: int) -> None:

            if curr_sum == target:
                res.append(curr_sol.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: #skip duplicates
                    continue
                if curr_sum + candidates[i] <= target:
                    curr_sol.append(candidates[i])
                    dfs(i + 1, curr_sum + candidates[i])
                    curr_sol.pop()
                else:
                    break #pruning (next there are only bigger elements --> always exceed target)
        
        dfs(0, 0)

        return res
