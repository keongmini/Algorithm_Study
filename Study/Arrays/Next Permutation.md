# leetcode 31. [Next Permutation](https://leetcode.com/problems/next-permutation/) (medium)

* 문제 해설 : 다음 순열 구하기  
  [Next Permutation Algorithm](https://github.com/keongmini/Today-I-Learned/blob/master/Algorithm/Next%20Permutation.md)
  
  example 1. 
  ```text
  Input: nums = [1,2,3]
  Output: [1,3,2]
  ```
  
  example 2. 
  ```text
  Input: nums = [1,1,5]
  Output: [1,5,1]
  ```
  
  제약조건.
  ```text
  1 <= nums.length <= 100
  0 <= nums[i] <= 100
  ```
  
* 문제 풀이 방법  
  참고 https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
  
  - 투포인터  
    **시간복잡도 O(N)**
    ```python
    class Solution:
        def nextPermutation(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
    
            i = j = len(nums) - 1
            
            while i > 0 and nums[i-1] >= nums[i]:       # 변화가 필요한 부분의 시작값 설정 
                i -= 1
                
            if i == 0:      # 전체 리스트가 내림차순이라는 뜻 == 순열의 마지막 -> 가장 작은 순열로 돌아감 
                nums.reverse()
                return
            
            k = i - 1       # 다음 순열에 필요한 값
            
            # 여기까지 진행할 경우, k 아래의 숫자들은 내림차순이라는 보장이 생김
            
            while nums[j] <= nums[k]:       # k 아래 내림차순으로 되어있는 숫자중 k와 가장 가깝게 큰 값 찾기 - 자리 변경해줄 값
                j -= 1
                
            nums[k], nums[j] = nums[j], nums[k]  
            l, r = k + 1, len(nums) - 1
            
            while l < r:        # 오름차순 -> 내림차순으로 바꾸기 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
    ```
  - 이분탐색  
    **시간복잡도 O(N)**
    ```python
    class Solution:
        def nextPermutation(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
    
            n = len(nums)
            i = n - 1
            while i > 0 and nums[i-1] >= nums[i]:
                i -= 1
            
            # 자리(순서)를 바꿔줄 값 찾기 
            if i > 0:
                left, right = i, n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[i-1] < nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                nums[i-1], nums[left-1] = nums[left-1], nums[i-1]
    
            # 뒤집기 
            left, right = i, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
    ```
 
