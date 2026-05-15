# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#!ITERATIVE BFS
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        queue = [root]

        idx = 0
        while True:
            if idx >= len(queue):
                break
            
            for _ in range(len(queue) - idx):
                r = queue[idx]
                idx += 1
                if isinstance(r, str):
                    continue

                if r.left:
                    queue.append(r.left)
                else:
                    queue.append("$")

                if r.right:
                    queue.append(r.right)
                else:
                    queue.append("$")

        
        return "#".join([str(r.val) if r != "$" else "$" for r in queue])

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split("#")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        
        i = 1
        while queue:
            node = queue.popleft()

            if i < len(values) and values[i] != "$":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            
            i += 1

            if i < len(values) and values[i] != "$":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            
            i += 1


        
        return root


#!RECURSUIVE DFS
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #!preorder visit
        res = []

        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return "#".join(res)

        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split("#")
        self.i = 0
        #same order
        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(int(values[self.i]))
            self.i += 1

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
        
       
            





        



