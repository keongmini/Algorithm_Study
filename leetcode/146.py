# 통과 - 효율성 좋지 않음
import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.length = capacity
        self.cache = {}
        self.key = collections.deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.key:
                self.key.remove(key)
            self.key.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.key.remove(key)
            self.key.append(key)
            self.cache[key] = value
            return

        if len(self.cache) == self.length:
            now = self.key.popleft()
            del self.cache[now]
        self.cache[key] = value
        self.key.append(key)

# 개선 풀이 - 이중연결리스트 + hashmap 구현
# O(1)
class DLinkedNode():  # 이중 연결리스트
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    def _add_node(self, node):
        # 노드를 가장 앞에 위치
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # 노드를 제거 -> 호출 되었거나 공간이 없어서 제거하기 위해
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)  # 현재 위치에서 제거
        self._add_node(node)  # 가장 앞에 위치

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key, None)  # key 값이 없으면 None 반환
        if not node:
            return -1

        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:  # 캐시 용량 초과로 가장 오래전 데이터 삭제
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:  # 원래 있던 key에 값과 위치만 바꿔줌
            node.value = value
            self._move_to_head(node)