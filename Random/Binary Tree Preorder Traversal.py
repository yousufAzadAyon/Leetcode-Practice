class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result, stack = [], []

        while stack or root:
            if root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right

        return result