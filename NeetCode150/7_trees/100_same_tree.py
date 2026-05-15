# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!RECURSIVE DFS, O(N) time and O(N) space
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True

        if not q or not p or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#!ITERATIVE DFS, O(N) time and O(N) space
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            p, q = stack.pop()

            if not p and not q:
                continue
            
            if not q or not p or q.val != p.val:
                return False
            
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        
        return True

#!ITERATIVE BFS, O(N) time and O(N) space
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            for _ in range(len(queue)): #one level traversal (not necessary here, but we care about it in zigzag traversal or level sums)
                p, q = queue.popleft()

                if not p and not q:
                    continue
                
                if not q or not p or p.val != q.val:
                    return False
                
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        
        return True






