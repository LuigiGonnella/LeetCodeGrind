#RECURSIVE DFS --> O(N) time and O(N) space (STACK)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root 

        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)

        root.left, root.right = root.right, root.left

        return root 

#ITERATIVE BFS --> O(N) time and O(N) space
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([])
        queue.append(root)

        while queue:
            #invert children
            r = queue.popleft()
            if r:
                r.left, r.right = r.right, r.left
                queue.append(r.left)
                queue.append(r.right)
            
        return root

#ITERATIVE DFS --> O(N) time and O(N) space (EXPLICIT STACK)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]
        while stack:
            r = stack.pop()
            r.left, r.right = r.right, r.left

            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left) 
        
        return root

