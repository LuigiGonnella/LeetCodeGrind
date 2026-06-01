
#!O(NlogN) time and O(1) extra-space
#GREEDY, SORTING
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        def notOverlap(int1, int2): #since int1[1] <= int2[1]
            return int2[0] >= int1[1]

        intervals.sort(key = lambda x: x[1]) #increasing ending time
        n = len(intervals)

        max_non_overlapping = 1
        curr = intervals[0]

        for interval in intervals[1:]:
            if notOverlap(curr, interval):
                max_non_overlapping += 1
                curr = interval
        
        return n - max_non_overlapping

            
        