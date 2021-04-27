class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def __init__(self):
        self.ans = True
        
    def dfs(self, root, depth):
        if(not root):
            return depth - 1 
        
        left = self.dfs(root.left, depth+1)
        right = self.dfs(root.right, depth+1)
        
        if(abs(left-right)>1):
            self.ans = False
        return max(left, right)
        
    def isBalanced(self, root: TreeNode) -> bool:
        self.dfs(root, 0)
        return self.ans

        