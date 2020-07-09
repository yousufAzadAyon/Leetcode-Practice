# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # (elem, level, number)
        level = [(root, 1)]
        width = 0
        while len(level) > 0:
            new_level = []
            if len(level) == 1:
                width = max(width, 1)
            left_node, left_n = level[0]
            right_node, right_n = level[-1]
            width = max(width, right_n - left_n + 1)
            for node, n in level:
                if node.left:
                    new_level.append((node.left, n*2))
                if node.right:
                    new_level.append((node.right, n*2+1))
            level = new_level
        return width