# TypeError: object of type 'ListNode' has no len()
# class Solution(object):
#     def isPalindrome(self, head):
#         for i in range(len(head)//2, len(head)):
#             if head[-1-i] != head[i]:
#                 return False
#
#         return True

# 리스트노드 -> 리스트 변환
class Solution(object):
    def isPalindrome(self, head):
        q = []

        if not head:
            return True

        while head:
            q.append(head.val)
            head = head.next

        for i in range(len(q)//2, len(q)):
            if q[-1-i] != q[i]:
                return False

        return True

# 데크 사용
import collections
class Solution(object):
    def isPalindrome(self, head):
        q = collections.deque()

        if not head:
            return True

        while head:
            q.append(head.val)
            head = head.next

        while len(q) > 1:
            if q.popleft() == q.pop():
                return False

        return True

# 스터디 풀이
class Solution(object):
    def isPalindrome(self, head):
        answer = []

        while head:
            answer.append(head.val)
            head = head.next

        return answer == answer[::-1]

s = Solution()
print(s.isPalindrome([1,2,2,1]))