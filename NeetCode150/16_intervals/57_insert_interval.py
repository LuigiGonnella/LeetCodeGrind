
#!O(N) time and O(1) extra space, LINEAR SEARCH, two passes
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def canOverlap(int1, int2):
            return max(int1[0], int2[0]) <= min(int1[1], int2[1])

        currInterval = newInterval
        indIdx = -1
        res = []
        idx = 0
        firstBigger = -1
         
        while idx < len(intervals):
            if intervals[idx][0] >= newInterval[0] and firstBigger == -1:
                firstBigger = idx
            if canOverlap(currInterval, intervals[idx]):
                while idx < len(intervals) and canOverlap(currInterval, intervals[idx]): #while can overlap, overlap and re-evaluate
                    if indIdx == -1:
                        indIdx = idx
                    currInterval = [min(currInterval[0], intervals[idx][0]), max(currInterval[1], intervals[idx][1])]
                    idx += 1
                
                res.append(currInterval)
            else:
                res.append(intervals[idx])
                idx += 1
        

        if indIdx == -1 and firstBigger == -1: #if no overlap was found and if no bigger start were found --> just append
            res.append(newInterval)
        elif indIdx == -1: #if no overlap but a bigger start was found --> insert in that position since there are no overlapping intervals but still we must maintain order
            res.insert(firstBigger, newInterval)
                
        return res

       

#!O(N) time and O(1) extra space, BINARY SEARCH --> O(N)
#we first found the correct position through binary search
#then we insert in the correct position (single pass) --> O(N)
#now we only need to merge with another pass --> O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        left, right = 0, len(intervals) - 1
        correctPos = len(intervals) #default is an append

        while left <= right:

            m = left + (right - left) // 2

            if intervals[m][0] < newInterval[0]: #go right
                left = m + 1
            else: #save and go left
                correctPos = m
                right = m - 1
        
        intervals.insert(correctPos, newInterval)

        res = []

        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else: #merge
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res



#!GREEDY --> SINGLE O(N) pass
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else: #merge
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        res.append(newInterval)
        
        return res












        