# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0
        def recur(root):
            nonlocal ans
            if not root:
                return True, 0
            if not root.left and not root.right:
                return False, 0
            
            lcover, lreach = recur(root.left)
            rcover, rreach = recur(root.right)
            
            if lcover and rcover:
                if lreach or rreach:
                    return True, 0
                else:
                    return False, 0
            else:
                ans += 1
                return True, 1
        
        cover, _ = recur(root)
        if not cover:
            ans += 1
        return ans