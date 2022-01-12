
//Definition for singly-linked list.
class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
 var getIntersectionNode = function(headA, headB) {
    let currA = headA,
        currB = headB;
    
    while(currA !== currB) {
        if(!currA) {
            currA = headB;
        } else {
            currA = currA.next;
        }
        if(!currB) {
            currB = headA;
        } else {
            currB = currB.next;
        }
    }
    return currA;
}
