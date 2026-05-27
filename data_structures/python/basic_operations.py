from collections import Counter
counts = Counter([1, 1, 2, 3]) # Result: Counter({1: 2, 2: 1, 3: 1})

from collections import defaultdict

d = defaultdict(list)
print(d)        # {}
d["a"]      # ✅ returns []

from collections import deque
q = deque([1, 2, 3])
q.popleft() # O(1) removal from the front

import heapq
min_heap = []
heapq.heappush(min_heap, 5)
smallest = heapq.heappop(min_heap)
h = heapq()
(priority, item) = 1, 2
heapq.heappush(h, (priority, item))

from functools import cache

class Solution:
    def fib(self, n: int) -> int:
        @cache # <--- This memoizes the function automatically!
        def dp(i):
            if i <= 1: return i
            return dp(i - 1) + dp(i - 2)
            
        return dp(n)
    
from collections import defaultdict, deque

# Given edges = [[0,1], [0,2], [1,2]]
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u) # If undirected

# Now adj[0] returns [1, 2]. 
# If you query a node with no edges, it safely returns an empty list [] instead of crashing.

a, b, curr, prev = 0, 0, 0, 0
# Swapping values
a, b = b, a 

# Linked list reversal in one line
curr.next, prev, curr = prev, curr, curr.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- How to use it in an interview ---

# 1. Building a Linked List: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# 2. Standard Traversal (O(N))
curr = head
while curr:
    print(curr.val)
    curr = curr.next

# 3. The "Dummy Node" Pattern (Crucial for edge cases)
# Use this when the head of the list might change or be removed.
dummy = ListNode(0)
dummy.next = head
curr = dummy

# ... perform operations ...
# return dummy.next

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- How to use it ---
# Building a Tree:
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# --- Standard Tree Traversals ---

# 1. Depth-First Search (DFS) - Recursive
def dfs_inorder(node):
    if not node:
        return
    dfs_inorder(node.left)
    print(node.val)         # Process node (In-order)
    dfs_inorder(node.right)

# 2. Breadth-First Search (BFS) / Level Order - Iterative
# Always use collections.deque for BFS!
def bfs(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue) 
        
        for _ in range(level_size):
            node = queue.popleft() # O(1) pop from front
            print(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)




from collections import defaultdict, deque

# Example Input: Undirected graph edges
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

# 1. Build the Adjacency List
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u) # Omit this line if the graph is DIRECTED

# Now adj looks like this: {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

# --- Standard Graph Traversals ---

# 2. Graph DFS (Recursive)
# Graphs have cycles, so we MUST track visited nodes using a set()
visited = set()

def graph_dfs(node):
    if node in visited:
        return
    
    visited.add(node)
    print(node) # Process node
    
    for neighbor in adj[node]:
        graph_dfs(neighbor)

# graph_dfs(0) # Start DFS from node 0

# 3. Graph BFS (Iterative)
def graph_bfs(start_node):
    queue = deque([start_node])
    visited_bfs = set([start_node])
    
    while queue:
        node = queue.popleft()
        print(node) # Process node
        
        for neighbor in adj[node]:
            if neighbor not in visited_bfs:
                visited_bfs.add(neighbor)
                queue.append(neighbor)

# graph_bfs(0) # Start BFS from node 0