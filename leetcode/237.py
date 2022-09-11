# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        cur = node.next
        while prev and cur and cur.next:
            prev.val = cur.val
            prev = prev.next
            cur = cur.next
        prev.val = cur.val
        prev.next = prev.next.next