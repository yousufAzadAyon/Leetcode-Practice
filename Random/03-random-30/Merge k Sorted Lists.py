# Definition for singly-linked list.
from typing import List
import heapq

class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def getElem(head):
            temp = []
            
            while head:
                temp.append(head.val)
                head = head.next
            
            return temp
        
        semifinal = []
        
        for x in range(len(lists)):
            semifinal.append(getElem(lists[x]))
        
        final = list(heapq.merge(*semifinal))
		
        if final:
            root = ListNode(final[0])
            node = root
            # root.next = ListNode(final[1])
            for x in range(len(final)-1):
                node.next = ListNode(final[x+1])
                node = node.next

            return root