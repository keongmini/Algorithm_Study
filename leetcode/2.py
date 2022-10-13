class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 단순 풀이
class Solution(object):
    def toList(self, head):
        nums = []

        if not head:
            return True

        while head:
            nums.append(str(head.val))
            head = head.next

        return int(''.join(list(reversed(nums))))

    def toLinkedList(self, list1):
        head = None
        for i in list1:
            node = ListNode(i)
            node.next = head
            head = node

        return node

    def addTwoNumbers(self, l1, l2):
        num1 = self.toList(l1)
        num2 = self.toList(l2)

        sumNum = str(num1 + num2)

        return self.toLinkedList(sumNum)

# 전가산기 풀이
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = head = ListNode(0)

        carry = 0 # 올라가는 수
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum+carry, 10)  # 10으로 나눌 때 몫과 나머지 한번에 반환
            head.next = ListNode(val)
            head = head.next

        return root.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = result = ListNode()
        carry = 0
        while l1 or l2:
            result.next = ListNode(carry)
            result = result.next

            if l1 and not l2:
                sumNum = l1.val + carry
                l1 = l1.next

            elif l2 and not l1:
                sumNum = l2.val + carry
                l2 = l2.next

            else:
                sumNum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            carry = sumNum // 10
            now = sumNum % 10

            result.val = now

        if carry:
            result.next = ListNode(carry)
            result = result.next
            result.val = carry

        return answer.next