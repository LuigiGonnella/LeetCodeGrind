
#!O(NlogS)
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l, r = max(nums), sum(nums)
        final = -1 

        def check(m: int) -> bool:

            curr = 0
            tot = 0

            for num in nums:
                curr += num
                if curr > m:
                    curr = num
                    tot += 1
            
            tot += 1 if curr else 0

            return tot <= k

        while l <= r:

            m = l + (r - l) // 2

            res = check(m) #False if not possible to form k subarrays up to sum m each (because they are more), True otherwise

            if not res:
                l = m + 1
            else:
                final = m
                r = m - 1
        
        return final


        