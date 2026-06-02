
#BRUTE FORCE
#!O(I * Q)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key = lambda x: x[1] - x[0]) #increasing duration --> O(IlogI)
        #we could also avoid sorting and simpling keep track of the minimum duration inteval, still O(I * Q)

        res = []
        for q in queries:
            found = False
            for interval in intervals:
                if q >= interval[0] and q <= interval[1]:
                    res.append(interval[1] - interval[0] + 1)
                    found = True
                    break

            #if no interval exists
            if not found:
                res.append(-1)
        
        return res


#SWEEP LINE ALGORITHM
#!O(I + Q) * log(I + Q)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        events = [] #collects intervals and queries events

        #POPULATE INTERVALS EVENTS
        for idx, (start, end) in enumerate(intervals):
            events.append((start, 0, end - start + 1, idx)) #0 indicates a start event
            events.append((end, 2, idx)) #2 indicates and end event
        
        #POPULATE QUERIES EVENTS
        for i, q in enumerate(queries):
            events.append((q, 1, i)) #1 indicates a query event
        
        #sort by time and type so QUERY is before END (since inclusive end we want to process first query and then mark as inactive that value)
        events.sort(key = lambda x: (x[0], x[1]))

        #min heap to store (size, index) --> tracks shortest intervals
        sizes = []
        #finals result array
        ans = [-1] * len(queries)
        #tracks inactive intervals to pop them from heap
        inactive = [False] * len(intervals)



        #we sweep over the TIME (in events) --> every time we get an eleemt
        #if it is a start --> push in heap
        #if it is an end --> mark inactive
        #if it is a query --> pop until the first active comes --> add to result
        for time, ev_type, *rest in events: #O(I + Q) * log(I + Q)
            if ev_type == 0: #start
                interval_size, idx = rest
                heapq.heappush(sizes, (interval_size, idx))
            elif ev_type == 2: #end
                idx = rest[0]
                inactive[idx] = True
            else: #query
                query_idx = rest[0]
                while sizes and inactive[sizes[0][1]]:
                    heapq.heappop(sizes)
                if sizes:
                    ans[query_idx] = sizes[0][0]
            
        
        return ans
            

#MIN_HEAP
#!O(IlogI + QlogQ)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:         
        intervals.sort()

        sorted_queries = sorted(queries)
        minHeap = []
        res = {}
        i = 0
        for q in sorted_queries: #for every query
            while i < len(intervals) and intervals[i][0] <= q: #this will be a global while, we will check only once each interval, adding the ones starting before the current query
            #since we sorted only on start, we cannott check in this while r >= q otherwise we could exit before considering valid intervals
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q: #since the queries are sorted and we added eevry possible intervals starting before this query
            #if and end is < q we can safely pop it since it will be < then any other query coming aftewards
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries] #maintain same order in the result



class SegmentTree:
    def __init__(self, N):
        self.size = N
        self.tree = [float("+inf")] * (4 * N) #4 * N is the upper bound of nodes to construct a balanced tree (every node has left and right child) from N elements in an array
        self.lazy = [float("+inf")] * (4 * N)
    
    def _propagate(self, treeidx, lo, hi): #when we update [lo, hi] we should check if the new val is actually the new minimujm for all of the elements in [lo, hi]
        #but we do this only when we visit them
        #!when we visit (UPDATE or QUERY) a node having pending updates, we update it --> NEW MINIMUM in this range
        if self.lazy[treeidx] != float("+inf"): #if there are pending updates for this node
            self.tree[treeidx] = min(self.tree[treeidx], self.lazy[treeidx])
            if lo != hi: #if not a point but a valid range --> add PENDING UPDATE to children since lazy contains a NEW VALUE that COULD BE THE NEW MINIMUM for the children too 
                self.lazy[2 * treeidx + 1] = min(self.lazy[2 * treeidx + 1], self.lazy[treeidx])
                self.lazy[2 * treeidx + 2] = min(self.lazy[2 * treeidx + 2], self.lazy[treeidx])
            
            self.lazy[treeidx] = float("+inf")
    
    def _update(self, treeidx, lo, hi, left, right, val): #!O(KlogK) with K = unique points
        #!we want to update the range [left, right] to set a NEW MINIMUM VAL, visiting [lo, hi] (initial values are 0 and N - 1)
        self._propagate(treeidx, lo, hi) #first we propagate pending updates in the current node, since we are visiting it

        ###! CASE 1 ### --> OUT OF BOUNDS
        if lo > right or hi < left: #if visiting range is outside the update range
            return
        
        ###! CASE 2 ### --> COMPLETE OVERLAP --> visiting range is completely included in update range
        if lo >= left and hi <= right: #!the lazy population (to be inherited by children) is only triggered when ALL VISITING RANGE is inlcuded in update range!!
            self.lazy[treeidx] = val #!lazy update --> since ALL [lo, hi] is covered by this update --> we should DO EVERY COMPARISON between this new VAL and all the values in this range
            #but we will do in a lazy way, when we will visit them
            self._propagate(treeidx, lo, hi) #propagate to current and add lazy to children (we also could have just updated current and wait for next visit to current to propagate lazy)
            return

        ###! CASE 3 ### --> PARTIAL OVERLAP --> visit both ends
        mid = lo + (hi - lo) // 2
        self._update(2 * treeidx + 1, lo, mid, left, right, val)
        self._update(2 * treeidx + 2, mid + 1, hi, left, right, val)

        self.tree[treeidx] = min(self.tree[2 * treeidx + 1], self.tree[2 * treeidx + 2]) #update parents back from recursion
    

    #!O(KlogK) with K = unique points
    def _query(self, treeidx, lo, hi, idx): #POINT QUERY --> which is the MINIMUM in IDX? we could also do this for a range query

        self._propagate(treeidx, lo, hi) #!--> this ensures leaf population even if we didn't explicit populate them with an update_range

        if lo == hi: #point range
            return self.tree[treeidx]
        
        mid = lo + (hi - lo) // 2

        if idx <= mid: #go left
            return self._query(treeidx * 2 + 1, lo, mid, idx)

        #go right
        return self._query(treeidx * 2 + 2, mid + 1, hi, idx)
    
    def update_range(self, left, right, val):
        return self._update(0, 0, self.size - 1, left, right, val)
    
    def query_point(self, idx):
        return self._query(0, 0, self.size - 1, idx)


#MIN SEGMENT TREE - LAZY PROPAGATION of range updates
#!#O(IlogK + #QlogK) time and O(K) space
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]: 
        points = set()

        for start, end in intervals: #O(I)
            points.add(start)
            points.add(end)
        
        for q in queries: #O(Q)
            points.add(q)
        
        points = sorted(points) #sorted LIST  O(KlogK)
        
        #es:
        # intervals = [[1,3],[2,3],[3,7],[6,6]]
        # queries = [2,3,1,7,6,8]
        # --> points = [1, 2, 3, 6, 7, 8]


        compress = {points[i]: i for i in range(len(points))}

        # --> compressed = {1:0, 2:1, 3:2, 6:4, 7:5, 8:6}

        segTree = SegmentTree(len(points))

        for interval in intervals: #O(IlogK)
            start = compress[interval[0]]
            end = compress[interval[1]]
            length = interval[1] - interval[0] + 1
            segTree.update_range(start, end, length) #add to segtree
        
        #at the end will be 

        ans = []
        for q in queries: #O(QlogK)
            idx = compress[q]

            res = segTree.query_point(idx)
            ans.append(res if res != float('inf') else -1)
        
        return ans

















