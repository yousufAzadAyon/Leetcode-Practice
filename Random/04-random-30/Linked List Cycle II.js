/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */

var detectCycle = function(head) {
    let slow = head;
    let fast = head;
    
    const detectIfLoop = () => {
        while(fast){
            if(fast.next && fast.next.next){
                slow = slow.next;
                fast = fast.next.next;
            }
            else fast = null;
            if(fast == slow) return true;
        }
        return false;
    }
    
    let loopExists = detectIfLoop();
    
    if(!loopExists) return null;
    else {
       let slow = head;
        while(slow != fast){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
    
};
