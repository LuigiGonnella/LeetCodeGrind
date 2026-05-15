# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#!RECURSIVE DFS --> O(N) time and O(N) space
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root: Optional[TreeNode], maxAnc: int) -> int:
            if not root:
                return 0

            isGood = 0
            if root.val >= maxAnc:
                maxAnc = root.val
                isGood = 1 

            lcnt = dfs(root.left, maxAnc)
            rcnt = dfs(root.right, maxAnc)

            return lcnt + rcnt + isGood
    
        return dfs(root, root.val)

#!ITERATIVE BFS --> O(N) time and O(N) space
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        maxAnc = float("-inf")
        queue = deque([(maxAnc, root)])

        while queue:
            maxAnc, r = queue.popleft()

            if r.val >= maxAnc:
                res += 1
            
            if r.left:
                queue.append((max(maxAnc, r.val), r.left))
            
            if r.right:
                queue.append((max(maxAnc, r.val), r.right))
        
        return res







        