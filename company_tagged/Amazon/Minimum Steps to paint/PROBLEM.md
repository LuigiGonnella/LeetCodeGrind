# Code Question 2

Amazon is introducing an innovative smart canvas display for personalized home decor. The canvas is initially painted white, featuring `n` rows and `m` columns, waiting to be transformed into a beautiful masterpiece.

Each minute, the canvas undergoes a unique coloring process as specified by the user.

A beautiful canvas is defined by the presence of a square with side length `k`, where all cells within the square are colored.

Determine the minimum time required for the canvas to achieve its beauty.

---

## Formal Description

Given:

- `n`: the number of rows of the canvas
- `m`: the number of columns of the canvas
- `k`: the side length of the square
- `paint`: a 2D array of dimensions `(n * m) x 2`

Each entry:

```text
paint[i][0], paint[i][1]
````

represents the coordinates of a cell to be painted black during the `i-th` minute.

Each cell is painted only once during the transformation.

Find the minimum time, in minutes, after which the canvas becomes beautiful.

---

## Example

```text
n = 2
m = 3
k = 2

paint = [[1, 2], [2, 3], [2, 1], [1, 3], [2, 2], [1, 1]]
```

Let `W` represent a white cell and `B` represent a black cell.

| Minute | Painted Cell        | Canvas Coloring | Beautiful                                   |
| -----: | ------------------- | --------------- | ------------------------------------------- |
|      1 | `paint[1] = (1, 2)` | `WBW`<br>`WWW`  | No                                          |
|      2 | `paint[2] = (2, 3)` | `WBW`<br>`WWB`  | No                                          |
|      3 | `paint[3] = (2, 1)` | `WBW`<br>`BWB`  | No                                          |
|      4 | `paint[4] = (1, 3)` | `WBB`<br>`BWB`  | No                                          |
|      5 | `paint[5] = (2, 2)` | `WBB`<br>`BBB`  | Yes, square starts at `(1, 2)`              |
|      6 | `paint[6] = (1, 1)` | `BBB`<br>`BBB`  | Yes, squares start at `(1, 1)` and `(1, 2)` |

After the `5th` and `6th` minutes, the canvas has a square of size `2 x 2` with all black cells.

At minute `5`, there is a valid square starting at position `(1, 2)`.

At minute `6`, there are valid squares starting at positions `(1, 1)` and `(1, 2)`.

Therefore, the minimum time after which the canvas becomes beautiful is:

```text
5
```

