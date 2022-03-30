class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        root = answer = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    value = list1.val
                    list1 = list1.next
                else:
                    value = list2.val
                    list2 = list2.next
            elif list1:
                value = list1.val
                list1 = list1.next
            elif list2:
                value = list2.val
                list2 = list2.next

            answer.next = ListNode(value)
            answer = answer.next

        return root.next        # leetcode 시스템 형식

# 스터디 풀이
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        root = answer = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                answer.next = ListNode(list1.val)
                answer = answer.next
                list1 = list1.next
            else:
                answer.next = ListNode(list2.val)
                answer = answer.next
                list2 = list2.next
        if list1:
            answer.next = list1
        if list2:
            answer.next = list2

        return root.next

# leetcode solution(재귀)
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2