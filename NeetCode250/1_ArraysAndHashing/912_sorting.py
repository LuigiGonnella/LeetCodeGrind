
#!O(NlogN) time and O(1) space HEAP SORT
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def getLeft(i):
                return 2 * i + 1

        def getRight(i):
            return 2 * i + 2
        
        def getParent(i):
            return (i - 1) // 2

        def heapify(nums, i, n): #O(logN)

            left = getLeft(i)
            right = getRight(i)

            maxEl = i

            if left < n:
                maxEl = maxEl if nums[maxEl] > nums[left] else left
            
            if right < n:
                maxEl = maxEl if nums[maxEl] > nums[right] else right
            
            if maxEl != i: #swap 
                nums[i], nums[maxEl] = nums[maxEl], nums[i]
                heapify(nums, maxEl, n) #recurr on swapped element
        
        def heapbuild(nums, n): #O(N)
            p = getParent(n - 1)
            for i in range(p, -1, -1):
                heapify(nums, i, n)
        
        heapbuild(nums, n)

        while n > 1:
            nums[0], nums[n - 1] = nums[n - 1], nums[0]
            n -= 1
            heapify(nums, 0, n)
        
        return nums
        

import random
#!O(NlogN) average time (N^ 2 worst) and O(1) space QUICK SORT
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, l, r):
            pivot_idx = random.randint(l, r - 1) #random pivot instead of last, but then i switch last
            nums[pivot_idx], nums[r - 1] = nums[r - 1], nums[pivot_idx]
            pivot = nums[r - 1]

            i, j = l - 1, r - 1
            
            while i < j:

                while i < r:
                    i += 1
                    if nums[i] >= pivot:
                        break
                
                while j >= 0:
                    j -= 1
                    if nums[j] < pivot:
                        break
                
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            
            nums[i], nums[r - 1] = nums[r - 1], nums[i]
            return i

        
        def quicksort(nums, l, r):
            if l < r:
                p = partition(nums, l, r)
                quicksort(nums, l, p)
                quicksort(nums, p + 1, r)
        
        l, r = 0, len(nums)
        quicksort(nums, l, r)


        return nums

    
#!O(NlogN) time and O(N) space MERGE SORT
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def twoWayMerge(nums, l, r, m):
            i, j = l, m + 1
            res = []

            while i <= m and j <= r:
                if nums[i] < nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            
            while i <= m:
                res.append(nums[i])
                i += 1

            while j <= r:
                res.append(nums[j])
                j += 1
            
            nums[l:r + 1] = res
        
        
        def mergeR(nums, l, r):
            if l < r:
                m = l + (r - l) // 2
                mergeR(nums, l, m)
                mergeR(nums, m + 1, r)
                twoWayMerge(nums, l, r, m)
        
        l, r = 0, len(nums)
        mergeR(nums, l, r - 1)
        return nums








