# leetcode 410. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) (hard)

* 문제 해설 : 배열의 값을 k 구간으로 나눌때 구간의 합 중 최대값이 최소가 되는  구하기, 빈 구간이 되면 안됨

  example 1. 
  ```text
    Input: nums = [7,2,5,10,8], k = 2
    Output: 18
    Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
    ```
  
  example 2.
  ```text
    Input: nums = [1,2,3,4,5], k = 2
    Output: 9
    Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
    ```
  
  제약조건.
  ```text
    1 <= nums.length <= 1000
    0 <= nums[i] <= 106
    1 <= k <= min(50, nums.length)
    ```
  
* Solution 풀이
  - 이분탐색   
    참고. [python discussion solution](https://leetcode.com/problems/split-array-largest-sum/discuss/1899144/Python-Clean-Code-oror-Parametric-Search)
  
    합의 구간을 이분탐색해서 중앙값과 쪼개진 갯수를 반복적으로 확인하면서 합의 구간을 줄여주는 방식 
  
    **시간복잡도 O(nlogm)**
  
      ```python
        class Solution:
            def splitArray(self, nums: List[int], m: int) -> int:
                low = max(nums)     # low = 나올 수 있는 최소값, 빈구간은 있을 수 없기 때문에 배열 내의 가장 큰 값보다는 무조건 합이 크거나 같게 나옴 
                high = sum(nums)    # high = 나올 수 있는 최대값, k가 1일 경우에 전체 합이 답이 됨
                while low < high:
                    mid = (low + high) // 2
                    total = 0       # 구간별 숫자 합
                    count = 1       # 다음 값이 들어오기 전에 mid보다 작을 수 있는 개수 세기 => 구간 세기
                    for num in nums:
                        if total + num <= mid: 
                            total += num
                        else:
                            total = num
                            count += 1
                    if count > m:           # 주어진 구간보다 더 많은 구간으로 나눠졌으면 합이 더 커져야함
                        low = mid+1
                    else:                   # 주어진 구간보다 같거나 작게 쪼개졌으면 합이 더 작아질 수 있음 
                        high = mid
                        
                return high
    ```
  
* 다른 접근 방법
  - dp top down
  - dp bottom up  
    이분탐색이 훨씬 효율적임