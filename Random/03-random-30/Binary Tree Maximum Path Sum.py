# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_sum = float('-inf')
        def helper(node):
            nonlocal max_sum
            if not node.left and not node.right:
                max_sum = max(max_sum, node.val)
                return max(node.val, 0)
            left = right = 0
            if node.left:
                left = max(helper(node.left), 0)
            if node.right:
                right = max(helper(node.right), 0)
            max_sum = max(max_sum, left + right + node.val)
            return max(left, right) + node.val
        helper(root)
        return max_sum