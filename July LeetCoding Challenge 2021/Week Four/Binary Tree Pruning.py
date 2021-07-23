class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.left and not node.right and node.val == 0:
                return None

            return node
        
        return dfs(root)