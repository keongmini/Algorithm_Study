# leetcode 11. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (medium)

* 문제 해설 : n개의 벽 중 두 개의 벽 사이에 물을 채울 때 가장 많은 물의 양 구하기, 두 개의 벽 사이에 있는 벽 들은 무시

  example1. 
  ```text
  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49
  ```
  
  example2.
  ```text
  Input: height = [1,1]
  Output: 1
  ```
  
  제약조건.
  ```text
  n == height.length
  2 <= n <= 10^5
  0 <= height[i] <= 10^4
  ```

* 문제 접근 방법
  1. height의 시작점과 끝점 두개를 비교하며 더 작은 값과 두개의 점 사이의 거리를 저장
  1. 더 작은 값의 지점을 한 이동
  1. 저장한 값 중 가장 큰 값 출력
  
  **시간복잡도 O(N)**  
  **투포인터 방법**
  
  ```python
  class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        result = []
        while left < right:
            now = abs(right - left) * min(height[left], height[right])
            result.append(now)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max(result)
  ```

* 다른 풀이 방법
    - 스택을 이용한 완전탐색 풀이  
      O(N^2) - 시간초과 
      ```python
        class Solution:
          def maxArea(self, height: List[int]) -> int:
            stack = [height[0]]
            
            result  = []
            for i in range(1, len(height)):
                for j in range(len(stack)):
                    now = min(stack[j], height[i]) * (i - j)
                    result.append(now)
                    
                stack.append(height[i])
            
            return max(result)
      ```
