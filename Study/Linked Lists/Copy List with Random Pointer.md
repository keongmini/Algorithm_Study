# leetcode 138. [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) (medium)

* 문제 해설 : 주어진 연결리스트 deep copy 하기, 연결리스트는 next와 random을 가지고 있고 둘다 동일하게 복사하되 이전 노드를 가리키면 안됨, random 값은 None일 수 있음
  
  [deep copy vs shallow copy](https://hongl.tistory.com/m/274)
  
  example 1.
  ```text
  Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
  Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
  ```
  
  example 2.
  ```text
  Input: head = [[3,null],[3,0],[3,null]]
  Output: [[3,null],[3,0],[3,null]]
  ```
  
  제약조건.
  ```text
  0 <= n <= 1000
  -104 <= Node.val <= 104
  Node.random is null or is pointing to some node in the linked list.
  ```
  
* 문제 접근 방법  
  값만 가져와서 다시 Node 생성하고 이어 주려고 함 - val, next는 해당 방법으로 구현가능  
  random값도 동일한 값을 갖되 새로 생성된 연결리스트로 연결해야 함 -> 구현 x
 
* solution 풀이 
  - recursive(재귀 - 완전탐색)
    1. 노드 저장할 딕셔너리 선언
    1. 딕셔너리에 값이 없을 경우 기존 노드(key)와 새로운 노드(value) 저장
    1. next와 random 모두 재귀로 돌리면서 저장되어있으면 값 꺼내오기, 저장된 값이 없으면 생성해서 저장하는 과정 반복
    
    **시간복잡도 O(N)** 
    
    ```python
    """
    # Definition for a Node.
    class Node:
        def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random
    """
    class Solution:
        def __init__(self):
            self.visitedHash = {}
            
        def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            
            if head == None:
                return None
            
            if head in self.visitedHash:
                return self.visitedHash[head]
            
            node = Node(head.val)
            
            self.visitedHash[head] = node
            
            node.next = self.copyRandomList(head.next)
            node.random = self.copyRandomList(head.random)
            
            return node
    ```