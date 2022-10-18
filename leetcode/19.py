# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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

# 다시 풀어봄 - 이전 풀이와 동일
# Two pass algorithm
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = root = head

        cnt = 0
        while head:
            cnt += 1
            head = head.next

        if cnt == n:
            return root.next

        cnt -= n

        for i in range(cnt - 1):
            root = root.next

        root.next = root.next.next

        return node

# One pass algorithm
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node1 = dummy
        node2 = head

        for _ in range(n):
            node2 = node2.next

        while node2:
            node2 = node2.next
            node1 = node1.next
        node1.next = node1.next.next
        return dummy.next