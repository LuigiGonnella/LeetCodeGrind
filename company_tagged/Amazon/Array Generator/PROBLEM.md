# Array Generator Service

## Problem Description
Your project team is collaborating with a group of software testers who require an **Array Generator Service** to assist in generating test data and validating software functionality. 

The service takes an initial array of positive integers and generates a sequence of integers of length **m** based on a dynamic "availability" state that updates after each selection.

---

## Technical Specification

### Input Parameters
* **arr**: An array of **n** positive integers (0-indexed).
* **state**: A binary string of length **n** representing the initial availability of each element:
    * `'1'` indicates that the corresponding `arr[i]` is **available** for selection.
    * `'0'` indicates that `arr[i]` is initially **blocked**.
* **m**: An integer representing the exact number of operations (selections) to perform.

### Operations and State Dynamics
To generate an integer sequence **S**, you must perform exactly **m** operations. Each operation consists of the following steps:

1. **Selection**: Choose any currently available element from `arr` (where `state[i] == '1'`). The same element can be chosen multiple times across different operations.
2. **Append**: Append the selected element to the sequence **S**.
3. **State Update**: Update the availability string for the next operation. Any blocked element (`state[i] == '0'`) that is immediately preceded by an available element (`state[i-1] == '1'`) becomes available (`'1'`). This means availability propagates to the right by one position per operation.

### Objective
Find the **lexicographically largest** sequence **S** that can be obtained after exactly **m** operations.

> **Note on Lexicographical Order:** A sequence A is lexicographically larger than a sequence B if, at the first index where A[i] != B[i], we have A[i] > B[i]. To maximize this, we should greedily select the largest possible available element at each step.

---

## Walkthrough Example

### Input
* `arr = [10, 5, 7, 6]`
* `state = "0101"`
* `m = 2`

### Step-by-Step Execution

| Operation | Available Elements (Values) | Available Indices | Chosen Element | Reason for Selection | Updated State |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **Initial** | — | — | — | — | `"0101"` |
| **Step 1** | `{5, 6}` | `{1, 3}` | **6** | max(5, 6) = 6 | `"0111"` <br>*(Index 2 becomes available because state[1] == '1')* |
| **Step 2** | `{5, 7, 6}` | `{1, 2, 3}` | **7** | max(5, 7, 6) = 7 | `"0111"` <br>*(No new cells match the propagation condition)* |

### Output
* `S = [6, 7]`

**Comparison:** `[6, 7]` is lexicographically larger than alternatives like `[6, 6]`, `[5, 7]`, or `[5, 5]`.

---

## Constraints
* 1 <= n <= 10^5 (Length of the array and state string)
* 1 <= arr[i] <= 10^9 (Value of elements)
* 1 <= m <= 10^5 (Number of operations)
* `state` is a valid binary string containing only `'0'` and `'1'`.

---

