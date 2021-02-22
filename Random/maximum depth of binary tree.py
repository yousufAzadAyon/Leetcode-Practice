class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0

        while len(q)>0:
            depth += 1
            temp = []
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp

        return depth
