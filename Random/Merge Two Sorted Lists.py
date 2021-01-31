class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self,l1,l2):
        if l1 == None and l2 == None:
            return None
        if l1 == [] and l2 == []:
            return []
        if l1 == []:
            return l2
        if l2 == []:
            return l1

        root = ListNode()
        l3 = root

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
            print(l3.val)

        if l1 == None and l2 != None:
            l3.next = l2
        if l2 == None and l1 != None:
            l3.next = l1

        return(root.next)
