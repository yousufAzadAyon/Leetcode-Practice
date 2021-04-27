class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        node = root
        sub_sum = 0
        paths = []
        res = False

        def dfs(node, sub_sum, sum, paths):
            paths.append(node)
            nonlocal res 
            if not node.left and not node.right:
                if sub_sum + node.val == sum:
                    res = True
                    return
                else:
                    return

            if node.left:
                dfs(node.left, sub_sum + node.val, sum, paths)
            if node.right:
                dfs(node.right, sub_sum + node.val, sum, paths)

        dfs(node, sub_sum, sum, paths)
        return res
