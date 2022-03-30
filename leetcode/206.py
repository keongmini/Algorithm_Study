class Solution(object):
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            # prev에 node 즉, 연결리스트 자체가 들어옴

        return prev

'''
# while문 내에서 prev print한 결과
ListNode{val: 1, next: None}
ListNode{val: 2, next: ListNode{val: 1, next: None}}
ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}
'''