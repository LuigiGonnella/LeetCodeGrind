# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!ITERATIVE BFS --> O(N) time and O(N) space
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            for i in range(len(queue)):
                r = queue.popleft()

                if i == 0:
                    res.append(r.val)

                if r.right:
                    queue.append(r.right)
                if r.left:
                    queue.append(r.left)
        
        return res


#!RECURSIVE DFS --> O(N) time and O(N) space
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels = []

        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if not root:
                return
            
            if len(self.levels) == depth:
                self.levels.append(root.val)
            
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        
        dfs(root, 0)
        
        return self.levels





        