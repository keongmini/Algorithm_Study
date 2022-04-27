class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

import collections

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        # defaultdict: 존재하지 않는 인덱스로 조회를 시도할 경우 에러를 발생하지 않고 바로 디폴트 객체 생성

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # 값 추가
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            # 값 업데이트
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]

        # 연결리스트의 첫번째 노드 해당 값인 경우
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            # if p.next is None:
            #     self.table[index] = ListNode()
            # else:
            #     self.table[index] = p.next
            return

        # 연결리스트의 다른 노드를 확인해야 하는 경우
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next가
            # 해당 노드를 다음 노드의 next와 연결