# leetcode 322. [Coin Change](https://leetcode.com/problems/coin-change/) (medium)

* 문제 해설 : 동전 종류가 주어질 때 동전의 합이 amount가 되기 위한 동전 최소 개수 구하기, 만약 구할 수 없으면 -1 반환  

  example 1. 
  ```text
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
    ```
  
  example 2.
  ```text
    Input: coins = [2], amount = 3
    Output: -1
    ```
  
  example 3.
  ```text
    Input: coins = [1], amount = 0
    Output: 0
    ```
  
  제약조건.
  ```text
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104
    ```
  
* 문제 접근 방법  
  예를들어, 동전이 2이고 동전의 합이 6이 되어야 하는 경우에  
  -> 동전보다 작은 합은 나올 수 없으니까 2부터 6까지 반복문 진행
     1. 반복문의 첫번째 값인 2 에서 동전(2)만큼 빼주면 0 
     2. dp에서 0의 값은 초기에 0으로 되어있고 나머지 인덱스 자리는 최대값으로 되어있음
     3. dp[0] + 1 값과 dp[2]의 값 비교하여 더 작은 값을 dp[2]에 저장 => 현재 동전 2만큼 빼준 위치(0)에서 동전 2를 하나 더 추가하면 현재 구하고자 하는 값(2)을 구할 수 있기 때문에
     4. 해당 과정을 반복
     
  **DP(bottom-up)**  
  **시간복잡도 O(N * M)**
   
  ```python
    class Solution:
        def coinChange(self, coins: List[int], amount: int) -> int:
            dp = [10001 for _ in range(amount + 1)]
            dp[0] = 0
            
            for coin in coins:
                for money in range(coin, amount + 1):
                    prev = money - coin
                    if prev != 10001:
                        dp[money] = min(dp[prev] + 1, dp[money])
            
            return dp[amount] if dp[amount] != 10001 else -1
    ```

* 다른 접근 방법
    - dp : top dowm
    - bfs
 
참고. [이것이 취업을 위한 코딩테스트이다. 8.5 효율적인 화폐구성](https://github.com/keongmini/Algorithm_Study/blob/master/%EC%9D%B4%EC%B7%A8%EC%BD%94%ED%85%8C/8-5.py)