from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        depth_vals = defaultdict(list)        
        queue = [(root, 0)]
        curr_depth = 0
        for node, depth in queue:
            if not node:
                depth_vals[depth].append(None)
            if node:
                depth_vals[depth].append(node.val)
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
            if depth > curr_depth:
                if depth_vals[curr_depth] != depth_vals[curr_depth][::-1]:
                    return False
                else:
                    curr_depth = depth
        else:
            return True
