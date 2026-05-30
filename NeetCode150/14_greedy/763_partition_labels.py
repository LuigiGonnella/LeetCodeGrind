
#!O(N) time and O(1) space
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        if not s:
            return [0]

        intervals = {} #char: (start, end) --> O(26) space

        for i, char in enumerate(s): # --> O(N) time
            if char not in intervals:
                intervals[char] = [-1, -1]
                intervals[char][0] = i #start
            
            intervals[char][1] = i #end
        
        final_int = list(intervals.values())
        final_int.sort(key = lambda x: x[0]) #sorted intervals by increasing starting index --> O(26log26) --> constant
            
        merges = []
        first = final_int[0]
        
        for j in range(1, len(final_int)): #for each couple, if they are not compatible --> merge and continue, otherwise, add current and continue
            if final_int[j][0] <  first[1]:
                first = [first[0], max(first[1], final_int[j][1])]
            else:
                merges.append(first)
                first = final_int[j]
        
        merges.append(first)
            
        return [(merge[1] - merge[0] + 1) for merge in merges]
        


#!O(N) time and O(1) space
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #we keep track of the last occurrency of each element
        #then we re-terate to start a partition and we continue until the last occurrence of every element seen so far 
        #until we reach that point since we didn't see any othe char having a lastOccur bigger than the current
        lastOcc = {}
        for i, char in enumerate(s):
            lastOcc[char] = i
        
        res = []
        end = -1
        size = 0

        for i, char in enumerate(s):
            size += 1
            end = max(end, lastOcc[char])

            if end == i: #we saw every lastOcc present in this partition --> we can close it
                res.append(size)
                size = 0
        
        return res

        



        