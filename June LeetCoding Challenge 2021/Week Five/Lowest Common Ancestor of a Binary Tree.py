class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node: return 0

            lft = dfs(node.left)
            rgh = dfs(node.right)
            mid = node in [p, q]
            if lft + rgh + mid >= 2:
                self.Found = node

            return max(lft, mid, rgh)
        
        self.Found = None
        dfs(root)
        return self.Found