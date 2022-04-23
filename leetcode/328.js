/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

var oddEvenList = function(head) {
    
    if(!head){
        return head
    }
    
    let odd = head
    let even = head.next
    let tmp = head.next
    
    while (even && even.next){
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    }
    odd.next = tmp
    
    return head
};

// const로 하면 안됨
// head에 값이 없을 경우 체크 해줘야 함 
