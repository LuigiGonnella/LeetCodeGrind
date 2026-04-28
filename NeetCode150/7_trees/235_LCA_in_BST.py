# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!RECURSIVE DFS --> O(h) time and O(h) space (worst case is degenerated tree --> O(N) in both time and space)
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q:
            return None
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val == root.val or q.val == root.val or p.val > root.val or q.val > root.val:
            return root

        return self.lowestCommonAncestor(root.left, p, q)