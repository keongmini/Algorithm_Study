# leetcode 904. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) (medium)

* 문제 해설 : 과일 나무가 한줄로 이어져있음 - 차례대로 과일 유형을 나타내는 배열이 주어짐, 하나의 나무에서 한개의 과일만 얻을 수 있음, 바구니에 두가지 과일만 담을 수 있을 때 가장 많이 과일을 담을 수 있는 개수 구하기   
  -> 즉, 배열 내의 구간을 정할 때 해당 구간에는 두가지 숫자만 존재해야하고 최대 구간이어야 함

  example 1. 
  ```text
    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.
    ```
  example 2.
  ```text
    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].
    ```
  
  example 3.
  ```text
    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
    If we had started at the first tree, we would only pick from trees [1,2].
    ```
  
  제약조건.
  ```text
    1 <= fruits.length <= 105
    0 <= fruits[i] < fruits.length
    ```
  
* 문제 접근 방법  
  방문하는 과일나무의 개수를 차례대로 세서 방문 내역을 저장하고 새로운 값이 나오면 이전 방문 내역 중 가장 오래 전 방문 내역부터 삭제 하는 방식으로 구현하고자 했으나 구현 x  
  딕셔너리에 유형(key)과 방문횟수(value)를 저장하게 되면 제거하지 않아도 되는 개수 까지 제거될 수 있다고 생각(ex. 2,1,2,2,3 의 경우 맨 앞에 2는 제거되어야 하지만 1이후의 2는 제거될 필요없음)  
  -> 새로운 숫자가 나올때마다 방문내역을 새롭게 저장해야 한다고 판단  
  각 구간별로 개수를 구해서 최대값을 갱신  

* Solution 풀이
  - 브루타포스 : 과일나무가 시작하는 위치마다 모두 확인 -> O(n^2) 
  
  - 슬라이딩 윈도우 1  
    윈도우의 끝점을 계속 이동하면서 과일 나무가 2개 이상이 될때 마다 시작점 이동  
    [2,2,2,3,2,1,2,2] 일 경우 1이 나오기 전 구간(길이 5)이 최대이지만 최대값을 저장하는 것이 아니라 윈도우의 크기(5)는 유지하면서 이동 -> 구간만 따지면 과일 나무가 3개 있지만 크기는 과일나무 2개 있을 때 최대 크기가 유지됨(현재 구간에 과일나무가 2개 초과일 경우 계속 시작점을 땡겨주기 때문에)
  
    **시간복잡도 O(N)**
    
    ```python
    class Solution:
        def totalFruit(self, fruits: List[int]) -> int:
            basket = {}     # 과일나무별 등장 횟수 저장
            left = 0        # 시작점
            
            for right, fruit in enumerate(fruits):
                basket[fruit] = basket.get(fruit, 0) + 1        # 방문처리 - 횟수 + 1
    
                if len(basket) > 2:         # 두개 이상이 될 경우 시작점 이동 -> 현재 시작점 인덱스에 있는 값의 횟수 - 1
                    basket[fruits[left]] -= 1
    
                    if basket[fruits[left]] == 0:       # 횟수 없음 - 제거
                        del basket[fruits[left]]
                    left += 1       # 시작점 이동 
                    
            return right - left + 1
    ```
    
  - 슬라이디 윈도우 2  
    끝점을 이동하면서 계속 최대값 갱신(저장)  
    - 1번 풀이와 다른점 : 과일나무 개수가 2 이하가 될 때까지 시작점을 계속 땡겨줌, 순간마다 최대값을 확인하여 최대값 반환    
  
    **시간복잡도 O(N)**
    
    ```python
    class Solution:
        def totalFruit(self, fruits: List[int]) -> int:
            basket = {}
            max_picked = 0
            left = 0
            
            for right in range(len(fruits)):
                basket[fruits[right]] = basket.get(fruits[right], 0) + 1
                
                while len(basket) > 2:
                    basket[fruits[left]] -= 1
                    if basket[fruits[left]] == 0:
                        del basket[fruits[left]]
                    left += 1
                
                max_picked = max(max_picked, right - left + 1)
            
            return max_picked
    ```