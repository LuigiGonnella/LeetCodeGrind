"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


#!O(NlogN) time and O(1) space
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True 

        
        intervals.sort(key = lambda x: x.start)

        currEnd = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < currEnd:
                return False
            
            currEnd = interval.end
        
        return True