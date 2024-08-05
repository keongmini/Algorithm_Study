# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        root = head
        n = 0
        result = []

        while root:  # 길이 구하기
            n += 1
            root = root.next

        root = head
        q, r = divmod(n, k)

        for _ in range(k):
            now = ListNode()  # 맨 처음에는 의미 없는 값
            part = now

            for _ in range(q + (r > 0)):  # r > 0 일 경우 1씩 더해주는 듯
                now.next, root, now = root, root.next, root  # 흠..

            if r > 0: r -= 1

            now.next = None  # 끝부분 자르기
            result.append(part.next)

        return result

# 시간 복잡도 O(n)    q + (r > 0) -> 전체 길이 n 스캔 (k 무시 가능)
# 공간 복잡도 O(k)    result에 저장되는 개수, 각 파트는 기존 ListNode를 사용하기 때문에 무시


# 실패: Memory Limit Exceeded
class Solution:
    def splitListToParts(self, head, k: int):
        root = head

        n = 0
        while root:
            n += 1
            root = root.next

        result = []

        if k >= n:
            while head:
                node = ListNode(head.val)
                result.append(node)
                head = head.next

            for _ in range(k - n):
                result.append(None)

        else:
            q, r = divmod(k, n)

            while head:
                now = []
                time = q
                if r > 0:
                    time += 1
                    r -= 1

                for _ in range(time):
                    node = ListNode(head.val)
                    now.append(node)
                    head = head.next

                result.append(now)

        return result