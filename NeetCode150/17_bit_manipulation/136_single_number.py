#!O(N) time
#!O(1) extra-space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #use XOR operations to delete all duplicates and return the only single value
        res = 0
        for num in nums:
            res ^= num
        
        return res

        