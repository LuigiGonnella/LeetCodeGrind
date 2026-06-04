# Code Question 1

Data analysts at Amazon are analyzing the information gained when a model is trained with different arrangements of the same data.

For an array of `n` integers, `data`, an arrangement is represented using a permutation of the integers from `1` to `n`.

They observed that the information gained for some permutation `p` of `n` integer data is equal to:

```text
sum(i * data[p[i]])
````

for `1 <= i <= n`.

For example, if:

```text
data = [2, 4, 5, 3]
p = [2, 1, 3, 4]
```

then the information gained is:

```text
1 * data[2] + 2 * data[1] + 3 * data[3] + 4 * data[4]
= 1 * 4 + 2 * 2 + 3 * 5 + 4 * 3
= 4 + 4 + 15 + 12
= 35
```

Given the array `data`, find the lexicographically smallest permutation `p` such that the information gained for the given data is maximum.

## Lexicographical Order

A permutation `p` is considered lexicographically smaller than a permutation `q` if the first index `i` where:

```text
p[i] != q[i]
```

satisfies:

```text
p[i] < q[i]
```

---

## Example

Suppose:

```text
n = 3
data = [2, 1, 2]
```

All possible permutations and their information gains are:

| Permutation |             Information Gain |
| ----------- | ---------------------------: |
| `[1, 2, 3]` | `1 * 2 + 2 * 1 + 3 * 2 = 10` |
| `[2, 1, 3]` | `1 * 1 + 2 * 2 + 3 * 2 = 11` |
| `[1, 3, 2]` |  `1 * 2 + 2 * 2 + 3 * 1 = 9` |
| `[3, 1, 2]` |  `1 * 2 + 2 * 2 + 3 * 1 = 9` |
| `[2, 3, 1]` | `1 * 1 + 2 * 2 + 3 * 2 = 11` |
| `[3, 2, 1]` | `1 * 2 + 2 * 1 + 3 * 2 = 10` |

The maximum information gain is achieved by permutations:

```text
[2, 1, 3]
[2, 3, 1]
```

The lexicographically smaller permutation of the two is:

```text
[2, 1, 3]
```

Hence, the answer is:

```text
[2, 1, 3]
```

---

## Function Description

Complete the function:

```text
findOptimalPermutation
```

in the editor below.

### Parameters

```text
int data[n]
```

The given data points.

### Returns

```text
int[n]
```

The lexicographically smallest permutation for which the information gain is maximum.

---

## Constraints

```text
1 <= n <= 10^5
1 <= data[i] <= 10^9
```


