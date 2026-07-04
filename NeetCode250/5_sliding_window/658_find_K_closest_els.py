
#!O(NlogN + KlogK)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key = lambda s: abs(s - x))
        res = sorted(arr[:k])

        return res


#!O(N - K)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l, r = 0, len(arr) - 1

        while r - l + 1 > k:

            if abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
            else: #if equal, prefer the lowest (arr[l] since arr is sorted in asc order)
                 r -= 1
        
        return arr[l: r + 1]


#!O(N + K) 
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        minD = float("+inf")
        idx = -1

        for i in range(n): #find closest to x (if equal, prefer lowest)

            if abs(arr[i] - x) < minD:
                minD = abs(arr[i] - x)
                idx = i


        res = deque([arr[idx]])

        l = idx - 1 
        r = idx + 1

        while len(res) < k:

            if l >= 0 and r < n:

                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.appendleft(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.appendleft(arr[l])
                l -= 1

            elif r < n:
                res.append(arr[r])
                r += 1
        
        return list(res)


#!O(logN + K
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # 1. Use binary search to find lowest arr[r] >= x (O(logN))
        r = bisect.bisect_left(arr, x)
        l = r - 1
        
        # 2. Expand outwards until we encompass k elements (O(k))
        while (r - l - 1) < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            # If both pointers are valid, pick the closer one
            # (Tie-breaker: prefer the smaller value, which is arr[l])
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
                
        # 3. Return the slice (O(k))
        return arr[l + 1 : r]



            
        
