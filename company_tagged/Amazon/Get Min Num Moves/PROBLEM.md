# Code Question 1: Weight Lifting Equipment

Imagine you are shopping on Amazon.com for some good weight lifting equipment. The equipment you want has blocks of many different weights that you can combine to lift.

The listing on Amazon gives you an array, `blocks`, that consists of $n$ different weighted blocks, in kilograms. There are no two blocks with the same weight. The element `blocks[i]` denotes the weight of the $i$-th block from the top of the stack. You consider weight lifting equipment to be good if the block at the top is the lightest, and the block at the bottom is the heaviest.

More formally, the equipment with array `blocks` will be called **good weight lifting equipment** if it satisfies the following conditions (assuming the index of the array starts from 1):
* $\\text{blocks}[1] < \\text{blocks}[i]$ for all $(2 \\le i \\le n)$
* $\\text{blocks}[i] < \\text{blocks}[n]$ for all $(1 \\le i \\le n-1)$

In one move, you can swap the order of adjacent blocks. Find out the minimum number of moves required to form good weight lifting equipment.

---

### Example

Let the blocks be in the order:  
`blocks = [3, 2, 1]`

1. **First Move:** Swap the first and the second blocks. After swapping, the order becomes: `blocks = [2, 3, 1]`
2. **Second Move:** Swap the second and the third blocks. After swapping, the order becomes: `blocks = [2, 1, 3]`
3. **Third Move:** Swap the first and the second blocks. After swapping, the order becomes: `blocks = [1, 2, 3]`

Now, the array satisfies the condition after **3** moves.

---

### Function Description

Complete the function `getMinNumMoves` in the editor below.

`getMinNumMoves` has the following parameter:
* `int blocks[n]`: an array of distinct integers representing weights.

**Returns:**
* `int`: the minimum number of operations required.

---

### Constraints

* $2 \\le n \\le 10^5$
* $1 \\le \\text{blocks}[i] \\le 10^9$ for all $(1 \\le i \\le n)$
* `blocks` consists of completely distinct integers.

---

### Input Format For Custom Testing

The first line contains an integer, $n$, the number of elements in `blocks`.  
Each line $i$ of the $n$ subsequent lines (where $1 \\le i \\le n$) contains an integer representing `blocks[i]`.

---

### Sample Case 0

#### Sample Input For Custom Testing

```text
5
2
4
3
1
6
```

#### Sample Output

```text
3
```

## Explanation
The lightest block needs to move left (towards the top). The heaviest block is already in the correct position (at the bottom).

- Move 1: Swap the third and the fourth blocks: blocks = [2, 4, 1, 3, 6]

- Move 2: Swap the second and the third blocks: blocks = [2, 1, 4, 3, 6]

- Move 3: Swap the first and the second blocks: blocks = [1, 2, 4, 3, 6]