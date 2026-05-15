
#!MINE
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr_sol = []
        def dfs(start: int, k: int, curr_sum: int) -> None:
            if len(curr_sol) >= k:
                if curr_sum == target:
                    res.append(curr_sol.copy())
                if curr_sum < target:
                    self.can_continue = 1
                return 

            for i in range(start, len(nums)):
                if curr_sum + nums[i] <= target:
                    curr_sol.append(nums[i])
                    dfs(i, k, curr_sum + nums[i])
                    curr_sol.pop()
        
        k = 1
        while True:
            self.can_continue = 0
            dfs(0, k, 0)
            if not self.can_continue:
                return res
            k += 1
            
#!CLEAN
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr_sol = []
        def dfs(start: int, curr_sum: int) -> None:
            if curr_sum == target:
                res.append(curr_sol.copy())
                return

            for i in range(start, len(nums)):
                if curr_sum + nums[i] <= target:
                    curr_sol.append(nums[i])
                    dfs(i, curr_sum + nums[i])
                    curr_sol.pop()
        
   
        dfs(0, 0)
        return res
            