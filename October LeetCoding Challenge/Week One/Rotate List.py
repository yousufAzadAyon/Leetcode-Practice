class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        current = head
        n = 1
        while current.next:
            n += 1 
            current = current.next
        current.next = head

        idx = n - k%n
        i = 0 
        current = head

        while i < idx:
            previous = current 
            current = current.next
            i += 1

        previous.next = None 
        head = current

        return head