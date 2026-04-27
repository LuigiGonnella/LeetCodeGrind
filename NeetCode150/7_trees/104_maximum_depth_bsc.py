# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#RECURSIVE DFS --> O(N) time, O(H) (degenera in N se albero su un unico path, e logN se perfettamente bilanciato)
#quindi space O(N) come per invert tree
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         nl = self.maxDepth(root.left)
#         nr = self.maxDepth(root.right)

#         if nl > nr:
#             return nl + 1
        
#         return nr + 1

#ITERATIVE DFS --> O(N) time, O(H) (degenera in N se albero su un unico path, e logN se perfettamente bilanciato)
#quindi space O(N) come per invert tree
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         res = 0
#         stack = [[root, 1]]

#         while stack:
#             node, depth = stack.pop()
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, res + 1])
#                 stack.append([node.right, res + 1])

        
#         return res

#ITERATIVE BFS --> O(N) time, O(N) space
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         queue = deque([root])
#         maxD = 0
#         while queue:
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
                
#             maxD += 1
        
#         return maxD

##ITERATIVE BFS --> O(N) time, O(N) space
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        maxD = 0
        while queue:
            node, depth = queue.popleft()
            if node:
                maxD = max(maxD, depth)
                queue.append([node.left, depth + 1])
                queue.append([node.right, depth + 1])
                
        
        return maxD





        


























