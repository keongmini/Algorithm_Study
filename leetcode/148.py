# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. 병합 정렬 풀이
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

# 2. 파이썬 풀이 - 훨씬 효율적
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        nums = []

        while node:
            nums.append(node.val)
            node = node.next

        nums.sort()
        print(nums)

        node = head

        for i in range(len(nums)):
            node.val = nums[i]
            node = node.next

        return head