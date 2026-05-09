
#!O(N + KlogN)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(p[0]**2 + p[1]**2, p) for p in points]
        heapq.heapify(min_heap) #O(N)

        res = []

        for _ in range(k):
            p = heapq.heappop(min_heap) #O(logN)
            res.append(p[1])

        return res

# Quick Select
# Intuition
# We want the k closest points, but we do NOT need them sorted.

# This is a perfect use-case for QuickSelect, the same idea used in QuickSort's partition step:

# Pick a pivot point.
# Partition all points into:
# points closer than the pivot
# points farther than the pivot
# After partitioning, the pivot ends at its correct position in the final sorted order.
# If the pivot ends up at index p:
# If p == k, then the left side already contains the k closest points.
# If p < k, search the right half.
# If p > k, search the left half.
#!This avoids fully sorting the array and runs in average O(N) time and O(N^2) in worst time
class Solution:
    def kClosest(self, points, k):
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]