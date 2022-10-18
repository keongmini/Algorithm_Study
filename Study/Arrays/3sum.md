# leetcode 15. [3Sum](https://leetcode.com/problems/3sum/) (medium)

* 문제 해설 : 더해서 0이 되는 3개의 숫자 조합 모두 출력, 없는 경우 빈 배열 출력

  example 1. 
  ```text
  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]
  ```
  
  example 2.
  ```text
  Input: nums = [0,1,1]
  Output: []
  ```
  
  example 3. 
  ```text
  Input: nums = [0,0,0]
  Output: [[0,0,0]]
  ```
  
  제약조건.
  ```text
  3 <= nums.length <= 3000
  -105 <= nums[i] <= 105
  ```
  
* 문제 접근 방법  
  반복문을 돌면서 숫자 하나를 고정해놓고 두개의 숫자 합과 합해서 0이 되는 값을 구하려고 했으나 세개의 반복문을 이용하는 풀이여서 시간초과 예상  
  조합의 결과가 반복되면 안되는데 어떻게 확인해야할지 구현x (set을 사용하려고 했는데 배열 내 순서가 동일할 경우에만 동일한 값으로 보기 때문에 불가)  
  -> wrong answer
  
* solution 풀이
  - 투포인터  
    값 정렬 후 반복문을 돌면서 각 위치를 고정하고 이후의 값 끼리 two sum 하는 방식  
    two sum 요소는 작은값과 큰값 더하기 -> 합이 크면 큰 값을 한칸 이동 / 합이 작으면 작은 값을 한칸 이동    
    고정하는 값이 이전 값과 동일하면 넘어감  
    
    **시간복잡도 O(N^2)**
    ```python
    class Solution:
        def twosum(self, nums: List[int], i: int, result: List[List[int]]):
            left, right = i+ 1, len(nums) - 1
            while left < right:
                sumNum = nums[i] + nums[left] + nums[right]
                
                if sumNum < 0:
                    left += 1
                elif sumNum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            result = []
            
            for i in range(len(nums)):
                if nums[i] > 0:
                    break
                if i == 0 or nums[i - 1] != nums[i]:
                    self.twosum(nums, i, result)
            
            return result
    ```

* 엣지케이스
  - [-2, 0, 0, 2, 2] : left와 right의 자리를 옮겨도 동일한 값이 나오는 경우가 있음 -> 중복으로 결과값이 들어가게 됨 -> 이전값과 같을 경우 한칸 이동