class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        temp1 = l1 = ListNode(0)
        temp2 = l2 = ListNode(1)

        while head:
            if head.val < x:
                temp1.next = ListNode(head.val)
                temp1 = temp1.next

            else:
                temp2.next = ListNode(head.val)
                temp2 = temp2.next

            head = head.next
        temp1.next = l2.next
        return l1.next
