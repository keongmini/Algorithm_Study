class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 값 바꾸기
class Solution(object):
    def swapPairs(self, head):
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next   # node는 pair 첫자리를 가르킬때 사용하는 용

        return head     # 같은 연결리스트를 바라보고 있기 때문에 head 출력


class Solution(object):
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            # 자리 바꾸기 완료 (재연결)

            prev.next = b    # pair 자리 변경완료

            head = head.next
            prev = prev.next.next   # 다음 pair로

        return root.next

# 재귀 풀이
class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            # p.next = 결국 head.next.next
            # pair끼리 재귀를 돌면서 그 결과를 차례대로 return 하는 방식
            p.next = head
            return p
        return head