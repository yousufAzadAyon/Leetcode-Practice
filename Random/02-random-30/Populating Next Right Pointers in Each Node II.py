class Node:
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        queue = []
        if root:
            queue = [root, None]
        while queue:
            node = queue.pop(0)
            if node:
                if queue:
                    if queue[0] is None:
                        node.next = None
                    else:
                        node.next = queue[0]
            else:
                if queue and queue[0] is not None:
                    queue.append(None)
            if node and node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)
        return root