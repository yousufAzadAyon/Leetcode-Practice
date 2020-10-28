class Solution(object):
    def detectCycle(self, head):
        if head == None: return None
        if head.next == None: return None
        
        first = head.next
        second = head.next.next
        
        while first != second:
            
            if first == None: return None
            if first.next == None: return None
            if second == None: return None
            if second.next == None: return None
            
            first = first.next
            second = second.next.next
            
        first = head
        
        while first != second:
            first = first.next
            second = second.next
        return first