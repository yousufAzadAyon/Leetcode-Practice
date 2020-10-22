# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        depth = 0
        nextLevel = [root]
        while True:
            level = nextLevel
            depth += 1
            nextLevel = []
            for n in level:
                found = False
                if n.left:
                    nextLevel.append(n.left)
                    found = True
                if n.right:
                    nextLevel.append(n.right)
                    found = True
                if not found:
                    return depth
        return 0