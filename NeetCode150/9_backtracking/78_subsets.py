
#!powerset con disposizioni ripetute
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def disp_rip(pos):
            if pos >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[pos])
            disp_rip(pos + 1)

            subset.pop()
            disp_rip(pos + 1)
        
        disp_rip(0)
        return res
        