# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root):
        self.total = 0
        if not root:
            return 0 
        def dfs(node,binary):
            binary += str(node.val)
            if not node.left and not node.right:
                ind = 0
                for i in binary[::-1]:
                    self.total += int(i) * (2**ind)
                    ind+=1
            if node.left:
                dfs(node.left,binary)
            if node.right:    
                dfs(node.right,binary) 
        dfs(root,"")        
        return self.total