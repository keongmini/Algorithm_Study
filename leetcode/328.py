class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):

        if not head:
            return head

        result = node = head

        tmp = head.next

        while head:
            if not head.next:
                node.next = tmp
                break
            elif not head.next.next:
                head.next = None
                while True:
                    if not node.next:
                        node.next = tmp
                        break
                    node = node.next
                break
            else:
                head.next, head = head.next.next, head.next

        return result

# 홀짝 지정 후 반복
class Solution(object):
    def oddEvenList(self, head):

        if not head:
            return head

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        return head