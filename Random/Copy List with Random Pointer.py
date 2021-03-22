class Node:
    def __init__(self, x, next=None, random=None) -> None:
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        temp = {}
        this_head = head
        while head:
            temp[head] = Node(head.val)
            head = head.next

        head = this_head
        while head:
            pair = temp[head]
            pair.next = None if not head.next else temp[head.next]
            pair.random = None if not head.random else temp[head.random]
            head = head.next

        return None if not this_head else temp[this_head]