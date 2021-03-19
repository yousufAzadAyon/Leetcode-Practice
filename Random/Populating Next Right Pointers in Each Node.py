class Node:
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root: return
        queue = [root]
        while queue:
            newq = []
            next = None
            for node in queue:
                node.next = next
                next = node
                if node.right: newq.append(node.right)
                if node.left: newq.append(node.left)
            queue = newq
        return root