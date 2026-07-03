# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


#!O(logN) three times
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 1, n - 2

        while l <= r:

            m = l + (r - l) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else: # left < mid > rigth
                break
        
        peak = m

        l, r = 0, peak - 1

        while l <= r:
            m = l + (r - l) // 2

            val = mountainArr.get(m)

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        

        l, r = peak, n - 1

        while l <= r:
            m = l + (r - l) // 2

            val = mountainArr.get(m)

            if val < target:
                r = m - 1
            elif val > target:
                l = m + 1
            else:
                return m
        
        return -1



