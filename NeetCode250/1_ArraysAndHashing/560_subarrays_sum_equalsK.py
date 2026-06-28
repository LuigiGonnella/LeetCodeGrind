
#!O(N) time and space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int) #occurrecnies of prefix sums
        prefix_sums[0] = 1 #prefix sum 0 is always present
        res = 0

        prefix = 0 #prefix sum
        for num in nums:
            prefix += num
            

            if (prefix - k) in prefix_sums: #if I reached a sum if 6 and previously i reached a sum of 1, it means that I can have a subarray of 5 (k)
                res += prefix_sums[prefix - k]
            
            prefix_sums[prefix] += 1
            
            
        
        return res

            
        