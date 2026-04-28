# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!ITERATIVE BFS --> O(N) time and O(N) space
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = [] #not needed since we don't have rercursive calls --> just use a local variable

        if not root:
            return self.levels

        def bfs(root: Optional[TreeNode]) -> None: #nested function not needed since it'iterative and only called once 
            queue = deque([root])

            while queue:
                level = []
                for _ in range(len(queue)):
                    r = queue.popleft()
                    level.append(r.val)

                    if r.left:
                        queue.append(r.left)
                    if r.right:
                        queue.append(r.right)
                
                self.levels.append(level)

        bfs(root)
        return self.levels

#!RECURSIVE DFS --> O(N) time and O(N) space
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []

        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if not root:
                return
            
            if len(self.levels) == depth:
                self.levels.append([])
            
            self.levels[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)

        return self.levels







