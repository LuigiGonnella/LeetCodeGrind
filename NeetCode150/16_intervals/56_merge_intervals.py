
#!O(NlogN) time and O(1) extra space
#SORTING
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key = lambda x: x[0]) #sort by ascending start

        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else: #merge, start is already good, fix only end
                res[-1][1] = max(interval[1], res[-1][1])
        
        return res


#!O(NlogN) time and O(N) extra space
#SWEEP LINE ALGORITHM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int) #keeps track of how many STARTS at start and ENDS at end --> summing them we will get the CURRENTLY NOT FINISHED (active) intervals
        #this count will never go NEGATIVE, since at most there will be as much ended as started and we will cathc when this count goes to ZERO
        # when ZERO --> MERGED INTERVAL CLOSED --> add to solution

        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        res = []
        curr_interval = [] #will host a single [start, end] interval to add to the final solution
        have = 0 #count to keep track of currently active intervals --> when 0 we have our interval to add to res

        #to make this work, mp must be sorted --> O(NlogN)
        for time in sorted(mp): #iterate over keys = time of start/end
            if not curr_interval: #START catched
                curr_interval.append(time) #add START
            have += mp[time] #count currently active (adding/subtracting started/ended)

            if have == 0: #we procesed an entire MERGED inetrval --> ADD TO RES
                curr_interval.append(time) #add END
                res.append(curr_interval)
                curr_interval = [] #clear current_interval to catch next one
        
        return res


#!O(N + M) time and O(M) extra space with M = largest element in intervals[i][j]
#GREEDY
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        max_start = max([interval[0] for interval in intervals]) #get max start --> O(N)

        mp = [-1] * (max_start + 1) #track FARTHEST possible END (mp[i]) for the start i

        for start, end in intervals: #--> O(N)
            mp[start] = max(mp[start], end)
        
        farthest = - 1
        curr_interval = []
        res = []
        for start in range(max_start + 1):
            if mp[start] != -1: #start exist
                if not curr_interval:
                    curr_interval.append(start)
                farthest = max(mp[start], farthest)

            if start == farthest:
                curr_interval.append(farthest)
                res.append(curr_interval)
                farthest = - 1
                curr_interval = []

        if len(curr_interval) == 1:
            curr_interval.append(farthest)
            res.append(curr_interval)
        
        return res






