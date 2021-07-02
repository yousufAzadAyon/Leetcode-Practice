
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for i in range(k):
                    a = cur.next
                    b = cur
                    cur.next = pre
                    
                    pre = b  
                    cur = a
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next