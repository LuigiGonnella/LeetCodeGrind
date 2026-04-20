class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        PartA, PartB = nums1, nums2

        if len(PartB) < len(PartA): #A is the smallest
            PartA, PartB = PartB, PartA
        
        totLen = len(PartA) + len(PartB)
        half = totLen // 2

        lA, rA = 0, len(PartA) - 1
        

        while True:

            m = (lA + rA) // 2
            lB = half - m - 2

            PartALeft = PartA[m] if m >= 0 else float('-inf')
            PartARight = PartA[m+1] if m < len(PartA) - 1 else float('+inf')
            PartBLeft = PartB[lB] if lB >= 0 else float('-inf')
            PartBRight = PartB[lB+1] if lB < len(PartB) - 1 else float('+inf')

            
            if PartALeft <= PartBRight and PartBLeft <= PartARight:
                if totLen % 2 == 0:
                    return (max(PartALeft, PartBLeft) + min(PartARight, PartBRight)) / 2
                return min(PartARight, PartBRight)
        
            if PartALeft > PartBRight:
                rA = m - 1
            elif PartALeft < PartBRight:
                lA = m + 1