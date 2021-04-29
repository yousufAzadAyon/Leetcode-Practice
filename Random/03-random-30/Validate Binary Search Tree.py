class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        q = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            q.append(node.val)
            dfs(node.right)
        dfs(root)
        
        for i in range(1,len(q)):
            if q[i-1]>=q[i]:
                return False
        return True