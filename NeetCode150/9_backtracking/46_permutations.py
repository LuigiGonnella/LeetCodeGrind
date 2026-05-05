class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_sol = []
        mark = [False] * len(nums)

        def dfs():
            if len(curr_sol) == len(nums):
                res.append(curr_sol.copy())
                return
            
            for i in range(len(nums)):
                if not mark[i]:
                    mark[i] = True
                    curr_sol.append(nums[i])
                    dfs()
                    curr_sol.pop()
                    mark[i] = False

        dfs()

        return res