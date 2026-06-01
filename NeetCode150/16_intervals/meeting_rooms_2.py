"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#!O(NlogN) time and O(N) space
#HEAP tracks number of rooms required
#the idea is simply to ADD one room if OVERLAP
#and REMOVE ONE ROOM if NOT OVERLAP
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda x: x.start) #ascending starting time

        min_heap = [] #stores ending time

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start: #if the meeting finishing the earliest is finishing BEFORE (<=) the current meeting starts --> reuse same room (first pop and then push)
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval.end)
        
        return len(min_heap) #at the end its length will be the mionimum number of rooms required
            


#!O(NlogN) time and O(N) space
#SWEEP LINE ALGORITHM
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        mp = defaultdict(int)

        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        

        curr_active = 0 #currently active meeting
        max_active = 0 #max number of simultaneously active meetings --> this is the result (the minimum numbe rof rooms required to satisfy all meetings)
        
        for start in sorted(mp):

            curr_active += mp[start]
            max_active = max(max_active, curr_active)
        
        return max_active




        