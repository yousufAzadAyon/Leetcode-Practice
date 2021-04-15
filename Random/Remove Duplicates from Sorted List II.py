# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        import collections
        ans, temp, count = [], head, collections.defaultdict(lambda : 0)
        
        # counting the repeating numbers and mapping them to count values
        while temp is not None:
            count[temp.val] += 1
            temp = temp.next
            
        # traversing the list and getting rid of repeated elements
        temp = head
        while temp is not None:
            if not count[temp.val] > 1:
                ans.append(temp)
            temp = temp.next
            
        # maintaining the list order
        for i in range(len(ans) - 1):
            ans[i].next = ans[i + 1]
            
        # if ans is not empty return the listnode address
        if ans:
            ans[-1].next = None
            return ans[0]
        
        # else return none
        return None