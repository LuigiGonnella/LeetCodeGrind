# Minimum Operations to Sort Points by Weight (Greedy)

## Problem Statement

There are $n$ points on the x-axis. The $i$-th point initially has a weight of `weight[i]` and is located at position $i$.

In a single operation, the $i$-th point can be moved to the right by a distance of `dist[i]`. Find the **minimum number of operations** required to sort the points by their weights (i.e., when reading positions from left to right, the weights must appear in a non-decreasing order).

---

## Examples

### Example 1

* **Input:** * `weight = [3, 6, 5, 2]`
* `dist   = [4, 3, 2, 1]`


* **Output:** `5`

**Explanation:**

* Point 3 stays at position 3.
* Point 0 moves to position 4.
* Point 2 moves to position 6.
* Point 1 moves to position 7.
* **Final Positions (Left to Right):** Weight order becomes `2, 3, 5, 6` (Sorted! ✓)
* **Total Operations:** $0 + 1 + 2 + 2 = 5$

### Example 2

* **Input:**
* `weight = [2, 4, 3, 1]`
* `dist   = [2, 6, 3, 5]`


* **Output:** `4`

**Explanation:**

* Point 3 stays at position 3.
* Point 0 moves to position 4.
* Point 2 moves to position 5.
* Point 1 moves to position 7.
* **Final Positions (Left to Right):** Weight order becomes `1, 2, 3, 4` (Sorted! ✓)
* **Total Operations:** $0 + 2 + 1 + 1 = 4$

---

## Intuition

### 1. Understanding the Goal

We want to ensure that as you walk along the x-axis from left to right, the weights you encounter are in strictly non-decreasing order. Because points can **only move right** (never left), their relative target order is completely fixed by their weights.

### 2. The Core Insight: Who Goes Where?

The desired left-to-right order is determined by sorting the points by weight. The lightest point must end up as the leftmost point, and the heaviest must end up as the rightmost point. This establishes our strict **target ordering**.

### 3. Why Greedy Works

Once we establish the target order, we can process the points sequentially from left to right:

* **The lightest point never moves:** Moving it right would only force all subsequent points further right, causing a cascade of extra operations. Thus, its final position is its initial position.
* **Minimize each point's final position:** Each subsequent point must be placed strictly to the right of the previous point's final position ($\text{pos} > \text{prev\_pos}$). If it already satisfies this condition, we do nothing ($0$ operations). If it doesn't, we jump it forward the absolute minimum number of times necessary to clear the threshold.

---

## Mathematical Formulation

For a point with an initial position $\text{pos}$ and a step distance $d$, we want to find the minimum number of jumps $k$ required to clear the strictly greater threshold $\text{prev\_pos}$:

$$\text{pos} + k \times d > \text{prev\_pos}$$

Solving for $k$:

$$k > \frac{\text{prev\_pos} - \text{pos}}{d}$$

Using integer division, the minimum integer $k$ is calculated as:

$$k = \lfloor \frac{\text{prev\_pos} - \text{pos}}{d} \rfloor + 1$$

> **Note:** If $\text{pos} > \text{prev\_pos}$ initially, then $k = 0$ because no operations are required.

---

## Step-by-Step Walkthrough (Example 1)

* `weight = [3, 6, 5, 2]`
* `dist   = [4, 3, 2, 1]`

**Sorted Target Order by Weight:** 1. Point 3 ($w = 2$, $\text{pos} = 3$)
2. Point 0 ($w = 3$, $\text{pos} = 0$)
3. Point 2 ($w = 5$, $\text{pos} = 2$)
4. Point 1 ($w = 6$, $\text{pos} = 1$)

| Step | Point | Initial Position | Distance ($d$) | Required Condition | Operations ($k$) | New Position | Next Threshold ($\text{prev\_pos}$) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | Point 3 | 3 | 1 | None (First item) | `0` | 3 | **3** |
| **2** | Point 0 | 0 | 4 | $\text{pos} > 3$ | `(3 - 0) // 4 + 1 = 1` | $0 + 1 \times 4 =$ **4** | **4** |
| **3** | Point 2 | 2 | 2 | $\text{pos} > 4$ | `(4 - 2) // 2 + 1 = 2` | $2 + 2 \times 2 =$ **6** | **6** |
| **4** | Point 1 | 1 | 3 | $\text{pos} > 6$ | `(6 - 1) // 3 + 1 = 2` | $1 + 2 \times 3 =$ **7** | **7** |

**Total Operations:** $0 + 1 + 2 + 2 = 5$

---

## Why is this Optimal?

1. **Fixed Strategy:** The relative target order is immutable because it is governed strictly by the sorting properties of the weights.
2. **No Over-movement:** For each step, the local calculation yields the absolute minimal movement necessary to satisfy the sorting invariant. Moving a point any further to the right can only increase or equal the threshold for the next point, potentially forcing it (and subsequent points) to make more jumps.
3. **Local to Global:** This is a textbook **greedy chain argument**. Making the locally optimal choice at step $i$ guarantees the optimal baseline condition for step $i+1$, which ultimately yields global optimality.

---

## Complexity Analysis

| Complexity Type | Big-O Notation | Explanation |
| --- | --- | --- |
| **Time Complexity** | $O(n \log n)$ | Dominated by sorting the indices based on their weights. The subsequent greedy pass runs in linear $O(n)$ time. |
| **Space Complexity** | $O(n)$ | Required to store the sorted order of indices/points. |