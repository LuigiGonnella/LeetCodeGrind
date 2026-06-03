# Solution Intuition: Monotonic State Tracking

The standard approach to a Range Minimum Query (RMQ) with point updates is a **Segment Tree**, which yields an $O(N \log N)$ runtime. However, by exploiting a hidden mathematical invariant specific to this load-balancing strategy, we can optimize the solution to a lightning-fast **$O(N)$ total time complexity** using $O(1)$ state tracking.

---

## 1. The Core Invariant: Monotonicity

The entire solution hinges on a single, powerful fact: the array tracking server request counts (`assigned`) will **always remain monotonically non-increasing (sorted in descending order)**.

$$\text{assigned}[0] \ge \text{assigned}[1] \ge \text{assigned}[2] \ge \dots \ge \text{assigned}[n-1]$$

### Why it stays sorted:

1. **The Range is a Prefix:** Every incoming request specifies an upper bound $r$. This means we are always looking at a window starting from the very first server: `[0 ... r]`.
2. **The Leftmost Tie-Breaker:** When multiple servers share the minimum request count, the rules dictate that we *must* choose the server with the smallest ID (the leftmost one).

Because server `0` is included in *every single query range* and is always favored in a tie, it will always accumulate requests first. Server `1` can never surpass server `0`, server `2` can never surpass server `1`, and so on.

---

## 2. The Clustered Block Structure

Because the `assigned` array is strictly sorted from largest to smallest, all servers holding the exact same number of requests will naturally cluster together into **contiguous blocks**.

```text
Server IDs:       [ 0,  1,  2,  3,  4 ]
Request Counts:   [ 2,  1,  1,  0,  0 ]
                  └──┘ └────┘ └────┘
                 Block  Block  Block
                 of 2s   of 1s  of 0s

```

---

## 3. Shifting from $O(N)$ Scan to $O(1)$ Lookups

We can use this block structure to eliminate all searching and range traversal entirely.

### Finding the Minimum in $O(1)$

When a request arrives with an upper bound $r$, we evaluate the prefix `[0 ... r]`. Because values decrease continuously as you move to the right, **the absolute minimum value in any prefix window is guaranteed to be its final element**.

$$\text{Minimum Count} = \text{assigned}[r]$$

### Resolving Ties in $O(1)$

If multiple servers share this minimum value, we must choose the leftmost one. Since identical values form a contiguous block, the leftmost server with a given count is simply the **very first server at the start of that block**.

We can maintain an array `next_available` where `next_available[cnt]` stores the exact server ID where the block of size `cnt` begins.

---

## 4. The Dynamic Update Mechanics

When a request is assigned to a server, that server's request count increments by `1`. This causes it to "graduate" out of its current block and move into the next one.

### Walkthrough of an Assignment Step:

Assume our servers are in the state: `[2, 1, 1, 0, 0]`

1. A request arrives with $r = 2$.
2. **Identify Minimum:** `cnt = assigned[2]` $\rightarrow$ The minimum count in range `[0...2]` is `1`.
3. **Identify Leftmost Server:** `idx = next_available[1]` $\rightarrow$ Points to **Server 1**.
4. **Update State:** Server 1 gains a request. Its count changes from `1` to `2`.

```text
Before Update:  [ 2,  1,  1,  0,  0 ]  --> next_available[1] points to Server 1
After Update:   [ 2,  2,  1,  0,  0 ]  --> next_available[1] shifts to Server 2

```

By simply executing `next_available[cnt] += 1`, we smoothly slide the boundary of the block to the right. The array remains perfectly sorted, and the tracking pointers remain completely accurate for the next query.

---

## Complexity Analysis

* **Time Complexity:** $O(\text{num\_servers} + \text{len}(\text{requests}))$. Every single request is processed using basic array lookups and arithmetic operations, making the cost per request a constant $O(1)$.
* **Space Complexity:** $O(\text{num\_servers} + \text{len}(\text{requests}))$ to store the allocation state arrays and the final results array.