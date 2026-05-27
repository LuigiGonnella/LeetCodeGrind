class SegmentTree:
    def __init__(self, data): #array of elements
        self.n = len(data)
        self.data = data

        #allocate 4*N space to maintain balanced tree
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(1, 0, self.n - 1)
    
    #!O(logN)
    def _build(self, node, left, right):
        #Base case --> left = right means single element = leaf node
        if left == right:
            self.tree[node] = self.data[left] #!index zero always empty
            return

        mid = left + (right - left) // 2
        left_child = 2 * node
        rigt_child = 2 * node + 1

        #recursively build left and right tree
        self._build(left_child, left, mid)
        self._build(rigt_child, mid + 1, right)

        #store SUM (here we could also stored the max or whatever)
        self.tree[node] = self.tree[left_child] + self.tree[rigt_child]


    #! POINT UPDATE O(logN) --> to update an entire range we should call this K times --> O(NlogN)    
    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)
    
    def _update(self, node, left, right, idx, val):
        #FOUND ELEMENT
        if left == right:
            self.tree[node] = val
            self.data[idx] = val
            return 

        mid = left + (right - left) // 2
        left_child = 2 * node
        right_child = 2 * node + 1 

        if left <= idx <= mid:
            self._update(left_child, left, mid, idx, val)
        else:
            self._update(right_child, mid + 1, right, idx, val)
        
        #recalculate sum after update for alla ancestros
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, L, R):
        return self._query(1, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        # Scenario 1: Complete mismatch
        if R < start or end < L: #tree not included at all
            return 0

        # Scenario 2: Complete overlap
        if L <= start and end <= R: #all tree included --> return root (include all)
            return self.tree[node]

        # Scenario 3: Partial overlap
        mid = (start + end) // 2
        left_sum = self._query(2 * node, start, mid, L, R)
        right_sum = self._query(2 * node + 1, mid + 1, end, L, R)

        return left_sum + right_sum