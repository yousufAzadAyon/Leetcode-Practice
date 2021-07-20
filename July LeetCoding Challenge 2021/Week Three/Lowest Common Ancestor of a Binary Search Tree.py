# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def _helper(node, p_target, q_target):
            if p_target < node.val and q_target < node.val:
                return _helper(node.left, p_target, q_target)
            elif p_target > node.val and q_target > node.val:
                return _helper(node.right, p_target, q_target)
            else:
                return node
        return _helper(root, p.val, q.val)