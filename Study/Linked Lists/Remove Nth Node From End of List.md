# leetcode 19. [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (medium)

* 문제 해설 : 연결리스트가 주어질 때, 뒤에서 n번째 위치한 노드를 제거한 연결리스트 구하기

  example 1. 
  ```text
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
  ```
  
  example 2. 
  ```text
  Input: head = [1], n = 1
  Output: []
  ```
  
  example 3. 
  ```text
  Input: head = [1,2], n = 1
  Output: [1]
  ```

  제약조건.
  ```text
  The number of nodes in the list is sz.
  1 <= sz <= 30
  0 <= Node.val <= 100
  1 <= n <= sz
  ```
  
* 문제 접근 방법 
  1. 연결리스트의 총길이 구한후 뒤에서 n 번째 값의 위치 찾기
  1. 다시 연결리스트를 돌면서 위에서 찾은 위치에 있는 노드 제거

  **시간복잡도 O(N)**  
  **완전탐색 [Two Pass Algorithm]**
  
  ```python
    class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            node = root = head
            
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            
            if cnt == n:
                return root.next
            
            cnt -= n
            
            for i in range(cnt - 1):
                root = root.next 
            
            root.next = root.next.next
            
            return node
  ```

* 다른 접근 방법
  - One Pass Algorithm(완전탐색)  
    1. n만큼 head를 이동한 연결리스트 a, 다음 노드가 head로 연결되는 연결리스트 b 선언
    1. a가 끝날 때까지 a, b 이동 -> b의 위치가 제거되어야할 노드 전 위치에 옴
    1. 해당 노드 를 다다음 노드와 연결 (다음 노드 : 제거할 노드)
    
    **시간복잡도 O(N)**
    
    ```python
    class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode(0,head)
            node1 = dummy
            node2 = head
            
            for _ in range(n):
                node2 = node2.next
            
            while node2:
                node2 = node2.next
                node1 = node1.next
            node1.next = node1.next.next
            return dummy.next
    ```

* 엣지케이스
  - ([2,1], 2) : 뒤에서 n번째 값이 첫번째 값일 경우, 연결해줄 값이 없기 때문에 head의 위치를 옮기면 됨  