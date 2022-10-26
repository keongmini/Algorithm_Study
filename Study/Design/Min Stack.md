# leetcode 155. [Min Stack](https://leetcode.com/problems/min-stack/) (medium)

* 문제 해설 : 스택 구현 + 가장 작은 값 반환 구현하기  
  **O(1)의 시간복잡도로 해결해야함**
 
  example 1. 
  ```text
    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]
    
    Output
    [null,null,null,null,-3,null,0,-2]
    
    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    ```
  
  제약조건.
  ```text
    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.
    ```
  
* 문제 접근 방법   
  min 내장함수를 사용하여 현재 스택에서 가장 작은 값 반환
  
  **시간복잡도 getMin: O(N)** 효율성 좋지 않음
  
  ```python
    class MinStack:
    
        def __init__(self):
            self.stack = []
    
        def push(self, val: int) -> None:
            self.stack.append(val)
    
        def pop(self) -> None:
            return self.stack.pop()
    
        def top(self) -> int:
            return self.stack[-1]
    
        def getMin(self) -> int:
            return min(self.stack)
    ```

* Solution 풀이
  - Two Stack
    
    작은 값을 관리하는 stack 별도로 선언(minStack), 첫번째 값 추가 - 첫번째 값 입장에서는 현재까지 가장 작은 값이 본인이기 때문에  
    값 추가될 때 마다 현재 minStack의 마지막 값보다 작을 경우 추가 <-> 클 경우 pass - minStack은 최소값만 관리하기 때문에 현재 값이 최소값보다 크다면 저장해둘 필요없음  
    
      **시간복잡도 O(1)**
      ```python
        class MinStack:
        
            def __init__(self):
                self.stack = []
                self.minStack = []
        
            def push(self, val: int) -> None:
                self.stack.append(val)
                if not self.minStack or val <= self.minStack[-1]:
                    self.minStack.append(val)
        
            def pop(self) -> None:
                if self.stack[-1] == self.minStack[-1]:
                    self.minStack.pop()
                self.stack.pop()
        
            def top(self) -> int:
                return self.stack[-1]
        
            def getMin(self) -> int:
                return self.minStack[-1]
      ```
  