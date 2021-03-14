class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return []
        res = []
        def helper(node, currPath, target):
            nonlocal res
            currPath.append(node.val)
            if node.left is None and node.right is None and target == 0:
                res.append(currPath[:])
            
            if node.left:
                helper(node.left, currPath[:], target - node.left.val)
            if node.right:
                helper(node.right, currPath, target - node.right.val)
            
            currPath.pop()
        
        helper(node = root, currPath = [], target = sum-root.val)
        return res