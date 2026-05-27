class LazySegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)  # Stores the lazy updates
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return

        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push(self, node, start, end):
        """
        Helper function to pass pending updates down to children.
        """
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (start + end) // 2

            # 1. Update Left Child
            # Total sum increases by (number of elements in left child range) * val
            self.tree[2 * node] += (mid - start + 1) * val
            self.lazy[2 * node] += val

            # 2. Update Right Child
            # Total sum increases by (number of elements in right child range) * val
            self.tree[2 * node + 1] += (end - mid) * val
            self.lazy[2 * node + 1] += val

            # 3. Clear the lazy flag for the current node
            self.lazy[node] = 0

    #!O(logN) for both ranges and points (range with L = R)
    def update_range(self, L, R, val):
        self._update_range(1, 0, self.n - 1, L, R, val)

    def _update_range(self, node, start, end, L, R, val):
        # Scenario 1: Complete mismatch
        if R < start or end < L:
            return

        # Scenario 2: Complete overlap
        if L <= start and end <= R:
            # Update the current node's sum directly
            self.tree[node] += (end - start + 1) * val
            # If it's not a leaf, mark its children as lazy
            if start != end:
                self.lazy[node] += val
            return

        # Scenario 3: Partial overlap
        # Before recursing down, we must resolve/push down any pending updates at this node
        self._push(node, start, end)

        mid = (start + end) // 2
        self._update_range(2 * node, start, mid, L, R, val)
        self._update_range(2 * node + 1, mid + 1, end, L, R, val)

        # Recalculate parent value after children are updated
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query_range(self, L, R):
        return self._query_range(1, 0, self.n - 1, L, R)

    def _query_range(self, node, start, end, L, R):
        # Scenario 1: Complete mismatch
        if R < start or end < L:
            return 0

        # Scenario 2: Complete overlap
        if L <= start and end <= R:
            return self.tree[node]

        # Scenario 3: Partial overlap
        # Crucial step: push down updates before reading child values!
        self._push(node, start, end)

        mid = (start + end) // 2
        left_sum = self._query_range(2 * node, start, mid, L, R)
        right_sum = self._query_range(2 * node + 1, mid + 1, end, L, R)

        return left_sum + right_sum