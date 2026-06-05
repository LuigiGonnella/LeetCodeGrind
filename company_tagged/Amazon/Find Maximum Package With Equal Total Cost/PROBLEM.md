# Find Maximum Packages with Equal Total Cost

## Problem Description

You are given an array of integers, `itemCost`, where each element represents the cost of an individual item. Your goal is to group these items into the **maximum possible number of packages** such that every package has the exact same total cost.

### Rules:

1. **Package Size:** Each package can contain either **zero**, **one** or **at most two** items.
2. **Disjoint Sets:** Each item from the array can belong to **at most one** package.
3. **Equal Cost:** All created packages must sum up to the same target cost. The optimal target cost is not predefined; you must determine the target cost that maximizes the total package count.

---

## Examples

### Example 1

* **Input:** `itemCost = [1, 2, 3, 4, 5]`
* **Output:** `3`
* **Explanation:** We can choose a target package cost of `5`. The packages are:
* Package 1: `[5]` (Cost = 5)
* Package 2: `[1, 4]` (Cost = 1 + 4 = 5)
* Package 3: `[2, 3]` (Cost = 2 + 3 = 5)
* Total packages formed = 3.



### Example 2

* **Input:** `itemCost = [1, 1, 2, 2, 1, 4]`
* **Output:** `3`
* **Explanation:** We can choose a target package cost of `1`.
* Three individual packages can be formed using each item of cost `1`: `[1]`, `[1]`, `[1]`.
* Total packages formed = 3.

