
#!O(m + n) time and O(1) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        p1 = m - 1
        p2 = n - 1
        last = m + n - 1

        while p1 >= 0 and p2 >= 0 and last >= 0: #pick biggest and go next
            if nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
            
            last -= 1
        
        j = 0
        for i in range(p1 + 1, last + 1): #fill remaining element of nums2 in empty cells of nums1 (from p1 + 1 to last)
            if j <= p2:
                nums1[i] = nums2[j]
                j += 1