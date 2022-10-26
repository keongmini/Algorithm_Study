# leetcode 146. [LRU Cache](https://leetcode.com/problems/lru-cache/) (medium)

* 문제 해설 : LRU Cache를 사용하는 자료구조 구현하기  

  [LRU Cache](https://github.com/keongmini/Today-I-Learned/blob/master/Algorithm/LRU%20Cache.md)

  example 1. 
  ```text
    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]
    
    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
    ```
  
  제약조건.
  ```text
    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.
    ```
  
* 문제 접근 방법  
  deque를 사용하여 가장 최근에 사용한 값이 맨 뒤에 올 수 있도록 호출될 때마다 remove -> append  
  
  **시간복잡도 get: O(N), put: O(M + N)** 효율성이 좋지는 않음
  
  ```python
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
    ```
  
* 다른 접근 방법
  - 개선된 LRU Cache(이중 연결리스트 + hashmap)  
      가장 최근 호출값 Head, 가장 오래된 값 Tail로 해서 이중연결리스트 구현
      호출될 때마다 연결리스트 상태 바꿔줌(제거시에는 이전값과 다음값 연결, 최신 값으로 업데이트시 head로 설정)  
      
      **시간복잡도 O(1)**
      
      ```python
        class DLinkedNode():        # 이중 연결리스트
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
                self._remove_node(node)     # 현재 위치에서 제거 
                self._add_node(node)        # 가장 앞에 위치 
        
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
                node = self.cache.get(key, None)        # key 값이 없으면 None 반환 
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
        
                    if self.size > self.capacity:       # 캐시 용량 초과로 가장 오래전 데이터 삭제 
                        tail = self._pop_tail()
                        del self.cache[tail.key]
                        self.size -= 1
                else:                                   # 원래 있던 key에 값과 위치만 바꿔줌
                    node.value = value
                    self._move_to_head(node)
    ```