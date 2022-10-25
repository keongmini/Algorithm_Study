# leetcode 34. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (medium)

* 문제 해설 : 정렬된 리스트에서 target 값의 시작 위치와 끝 위치를 반환, 만약 리스트에 target 값이 존재 하지 않으면 [-1,-,1] 반환  
  **O(log n)의 시간복잡도로 해결해야함**
 
  example 1. 
  ```text
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
  ```
  
  example 2. 
  ```text
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
   ```
  
  example 3.
  ```text
    Input: nums = [], target = 0
    Output: [-1,-1]
  ```

  제약조건.
  ```text
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
  ```
  
* 문제 접근 방법  
  index 내장 함수를 사용하여 target의 시작 위치를 찾고 시작 위치부터 시작하여 target과 다른 값이 나올 때까지 반복문 진행

  **시간복잡도 O(N)** 최악의 경우 리스트의 모든 숫자가 target일 수 있으니..
  
  ```python
    class Solution:
        def searchRange(self, nums: List[int], target: int) -> List[int]:
            numset = set(nums)
            
            if target not in numset:
                return [-1, -1]
            
            start = nums.index(target)
            
            result = [start]
            
            for i in range(start, len(nums)):
                if nums[i] != target:
                    result.append(i - 1)
                    return result
            
            result.append(len(nums) - 1)
            return result
  ```
  
* Solution 풀이 
  - 이분탐색  
    시작점과 끝점을 각각 이분탐색으로 찾음   
    시작점일 경우 target 발견시 이전 값과 다른지 확인 - 첫번째 값임  
    끝점일 경우 target 발견시 이후 값과 다른지 확인 - 마지막 값임  
  
    **시간복잡도 O(log n)**
    
    ```python
    class Solution:
        def searchRange(self, nums: List[int], target: int) -> List[int]:
    
            lower_bound = self.findBound(nums, target, True)        # 시작점 찾기 
            if (lower_bound == -1):
                return [-1, -1]
    
            upper_bound = self.findBound(nums, target, False)       # 끝점 찾기
    
            return [lower_bound, upper_bound]
    
        def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
            
            N = len(nums)
            begin, end = 0, N - 1
            while begin <= end:
                mid = int((begin + end) / 2)
    
                if nums[mid] == target:
    
                    if isFirst:     # 시작점을 찾는 경우 
                        if mid == begin or nums[mid - 1] < target:
                            return mid
    
                        end = mid - 1
                    else:           # 끝점을 찾는 경우
                        if mid == end or nums[mid + 1] > target:
                            return mid
    
                        begin = mid + 1
    
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    begin = mid + 1
    
            return -1
    ```