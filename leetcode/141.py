# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        result = collections.defaultdict(list)

        while True:
            if not head:
                return False

            if head.next in result[head.val]:
                return True

            result[head.val].append(head.next)

            head = head.next
