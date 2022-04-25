# 배열을 이용한 풀이
class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = [None] * k
        self.maxLen = k
        self.front = 0
        self.last = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dq[self.front-1] = value
        self.front = (self.front - 1) % self.maxLen
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dq[self.last] = value
        self.last = (self.last + 1) % self.maxLen
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.dq[self.front] = None
        self.front = (self.front + 1) % self.maxLen
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.dq[self.last - 1] = None
        self.last = (self.last - 1) % self.maxLen
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[self.last - 1]

    def isEmpty(self) -> bool:
        return self.front == self.last and self.dq[self.front] == None

    def isFull(self) -> bool:
        return self.front == self.last and self.dq[self.front] != None

# 이중연결리스트를 이용한 풀이
class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
