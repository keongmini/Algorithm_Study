# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = start = head

        length = 0
        while root.next:
            length += 1
            root = root.next

        length -= n

        if length < 0:
            return head.next

        for i in range(length):
            start = start.next

        start.next = start.next.next

        return head