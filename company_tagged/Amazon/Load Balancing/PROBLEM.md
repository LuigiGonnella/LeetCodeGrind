# Prototype Load-Balancing Algorithm

## Problem Description

The developers of Amazon are working on a prototype for a simple load-balancing algorithm. There are `num_servers` servers numbered from `0` to `num_servers - 1`, and the initial number of requests assigned to each server is `0`.

In the $i^{\text{th}}$ second, a request comes from an IP hash of `requests[i]`. It must be assigned to the server with the **minimum number of requests** among the servers from index `0` to `requests[i]`.

* For example, if `requests[i] = 4`, the request must be assigned to the server with the minimum number of requests amongst the servers with IDs `[0, 1, 2, 3, 4]`.
* If there are multiple servers with the same minimum number of requests, choose the one with the **minimum ID**.
* When a request is assigned to a server, its number of requests increases by `1`.

Given `num_servers` and the array `requests`, find the ID of the server each request is assigned to.

---

## Function Description

Complete the function `findRequestTarget` in the editor below.

`findRequestTarget` takes the following arguments:

* `int num_servers`: the number of servers available.
* `int requests[n]`: an array of integers representing the upper bounds of the server choices for each request.

### Returns

* `int[n]`: an array of integers containing the IDs of the servers each request is assigned to.

---

## Constraints

* $1 \le \text{num\_servers} \le 10^5$
* $0 \le \text{requests}[i] < \text{num\_servers}$
* $1 \le n \le 10^5$

---

## Examples

### Example 1

* **Input:** `num_servers = 5`, `requests = [3, 2, 3, 2, 4]`
* **Output:** `[0, 1, 2, 0, 3]`

#### Walkthrough

| Step | Request IP Hash | Server Request Allocation State | Assigned To | Remarks |
| --- | --- | --- | --- | --- |
| **1** | `3` | `[0, 0, 0, 0, 0]` | **0** | The request must be assigned to the server with the minimum number of requests amongst the first 4 servers `[0, 1, 2, 3]`. Since all have 0 requests, choose the minimum ID `0`. |
| **2** | `2` | `[1, 0, 0, 0, 0]` | **1** | Look at servers `[0, 1, 2]`. Server 1 and 2 both have 0 requests, which is less than server 0 (1 request). Choose the minimum ID `1`. |
| **3** | `3` | `[1, 1, 0, 0, 0]` | **2** | Look at servers `[0, 1, 2, 3]`. Servers 2 and 3 both have 0 requests. Choose the minimum ID `2`. |
| **4** | `2` | `[1, 1, 1, 0, 0]` | **0** | Look at servers `[0, 1, 2]`. All three have exactly 1 request. Choose the one with the minimum ID `0`. |
| **5** | `4` | `[2, 1, 1, 0, 0]` | **3** | Look at all servers `[0, 1, 2, 3, 4]`. Servers 3 and 4 have 0 requests. Choose the minimum ID `3`. |

---

## Sample Cases

### Sample Case 0

#### Sample Input for Custom Testing

```text
num_servers = 5
requests = [4, 0, 2, 2]

```

#### Sample Output

```text
0
0
1
2

```

#### Explanation

* **Request 1 (`4`):** Scans servers `[0, 1, 2, 3, 4]`. All have 0 requests; goes to server `0`. State: `[1, 0, 0, 0, 0]`.
* **Request 2 (`0`):** Scans only server `[0]`. Must go to server `0`. State: `[2, 0, 0, 0, 0]`.
* **Request 3 (`2`):** Scans servers `[0, 1, 2]`. Servers 1 and 2 have 0 requests; goes to server `1`. State: `[2, 1, 0, 0, 0]`.
* **Request 4 (`2`):** Scans servers `[0, 1, 2]`. Server 2 has 0 requests; goes to server `2`. State: `[2, 1, 1, 0, 0]`.

### Sample Case 1

#### Sample Input for Custom Testing

```text
num_servers = 5
requests = [0, 1, 2, 3]

```

#### Sample Output

```text
0
1
2
3

```

#### Explanation

Each request $i$ is sequentially assigned to the first available index with a request count equal to `0`, corresponding exactly to the value of `requests[i]`.