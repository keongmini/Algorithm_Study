# leetcode 152. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (medium)

* 문제 해설 : 리스트 내에 연속된 값을 곱했을 때 나올 수 있는 가장 큰 값 구하기  

  example 1. 
  ```text
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    ```
  
  example 2.
  ```text
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    ```
  
  제약조건.
  ```text
    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    ```
  
* 문제 접근 방법  
  값의 합과 달리 두개의 음수 값을 곱하면 양수값이 나옴    
  확인해야하는 경우 - 양수x양수, 음수x음수  
  이전의 값을 4개 저장해야 한다고 판단 - 가장 큰 양수, 음수, 가장 큰 양수, 음수  
  -> 이후에 들어올 값이 어떤지 모르기 때문

* Soution 풀이

  - DP
  가장 작은 값과 가장 큰 값만 저장하면 됨  
  어떤 부호의 값이 들어올지 모르므로 가장 작은 값과의 곱, 가장 큰 값과의 곱, 해당 값 세개 비교  
  -> 음수일 경우, 가장 작은 값(음수라는 가장하에)과 만나면 최대값이 될 수 있음  
  
  **시간복잡도 O(N)**
  
  ```python
    class Solution:
        def maxProduct(self, nums: List[int]) -> int:
            if len(nums) == 0:
                return 0
    
            max_so_far = nums[0]
            min_so_far = nums[0]
            result = max_so_far
    
            for i in range(1, len(nums)):
                curr = nums[i]
                temp_max = max(curr, max_so_far * curr, min_so_far * curr)
                min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
    
                max_so_far = temp_max       # min_so_far 구하는 부분에서 바뀌기 전 max_so_far값 사용하기 위해 
    
                result = max(max_so_far, result)
    
            return result
    ```