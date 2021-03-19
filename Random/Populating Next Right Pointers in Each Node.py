class Node:
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
      if not root:
        return root
      node = root
      while node.left:
        head = node
        while head:
          if head.next:
            leftAdjacent = head.next.left
            head.right.next = leftAdjacent
          head.left.next = head.right
          head = head.next
        node = node.left
      return root