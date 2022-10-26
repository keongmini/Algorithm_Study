# leetcode 55. [Jump Game](https://leetcode.com/problems/jump-game/) (medium)

* 문제 해설 : 배열 각 자리에는 해당 인덱스에서 점프해서 최대로 갈 수 있는 거리가 주어짐, 점프해서 마지막 인덱스까지 도달할 수 있으면 true, 마지막 인덱스에 접근할 수 없으면 false
 
  example 1.
  ```text
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    ``` 
  
  example 2.
  ```text
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    ```
  
  제약조건.
  ```text
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5
    ```
  
* 문제 접근 방법  
  첫번째 자리부터 차례대로 점프할 수 있는 최대횟수까지 점프하면서 각 지점 방문 처리 - 마지막 인덱스에 도달하면 true 반환
  전체를 다 돌았는데도 마지막 인덱스가 방문처리 되지 않으면 false 반환
  -> 시간초과 
  
  **시간복잡도 O(N^2)** 
  
  ```python
    import collections
    class Solution:
        def canJump(self, nums: List[int]) -> bool:
            if len(nums) == 1:
                return True
            
            visited = [False for _ in range(len(nums))]
            dq = collections.deque([0])
            visited[0] = True
            
            while dq:
                now = dq.popleft()
                
                for i in range(nums[now]):
                    n = (now + 1) + i
                    if n < len(nums) and not visited[n]:
                        dq.append(n)
                        visited[n] = True
                    
                    if visited[len(nums) - 1]:
                        return True
            
            return False
    ```
  
* 다른 접근 방법
  - 배열
    
    반복문 돌면서 최대 길이 갱신해줌 - 만약 index가 최대 길이보다 큰 순간이 나오면 해당 인덱스까지 접근하지 못했음, 마지막 인덱스까지 접근할 수 없음 -> False  
    현재 인덱스(위치) + 해당 값 = 시작점부터 해당 인덱스를 거쳐 갈 수 있는 최대 거리
    
    **시간복잡도 O(N)**
    
    ```python
    class Solution:
        def canJump(self, nums: List[int]) -> bool:
            length = 0
            for i in range(len(nums)):
                if i > length:
                    return False
                
                length = max(nums[i] + i, length)
            
            return True
    ```