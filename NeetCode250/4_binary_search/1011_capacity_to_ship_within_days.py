
#!O(NlogN) time and O(1) space
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        tot = sum(weights)

        if days == 1:
            return tot
        
        maxEl = max(weights)

        def check(n: int) -> int:
            curr = 0
            tot_n = 0
            for num in weights:
                curr += num
                
                if curr == n:
                    tot_n += 1
                    curr = 0

                elif curr > n:
                    tot_n += 1
                    curr = num
            
            tot_n += 1 if curr else 0

            
            if tot_n > days:
                return -1
            
            if tot_n <= days:
                return 1


        l, r = maxEl, tot + 1

        res = -1

        while l < r:
            m = l + (r - l) // 2
            
            curr = check(m)
            

            if curr < 0:
                l = m + 1
            else:
                res = m
                r = m
        
        return res
        