# leetcode 247. [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/) (medium)

* 문제 해설 : 180도로 돌렸을 때 모양이 똑같은 n개 길이의 숫자 모두 찾기 
  > A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

  example 1. 
  ```text
  Input: n = 2
  Output: ["11","69","88","96"]
  ```
  
  example 2.
  ```text
  Input: n = 1
  Output: ["0","1","8"]
  ```
  
  제약조건.
  ```text
  1 <= n <= 14
  ```

* 문제 접근 방법
  앞뒤로 올 수 있는 숫자는 1, 6, 8, 9만 가능하고 0, 1, 8은 사이에 낄 수 있음(단독), 6-9는 서로 짝꿍  
  길이//2만큼 반복문을 돌면서 가능한 모든 경우에 대해 처리하면서 앞뒤로 숫자를 insert해주려고 했으나 구현x

* Solution 풀이 
  - 재귀 풀이 
    1. 주어진 길이에서 2개씩(양쪽) 제거하면서 가장 안쪽, 즉 가운데로 이동 (홀수 -> 1개 남는 시점, 짝수 -> 0개 남는 시점)
    1. 가장 안쪽부터 앞뒤로 값 추가하면서 재귀적으로 진행
    
    **시간복잡도 O(N⋅5^([N/2]+1))**
    
    ```python
    class Solution:
        def findStrobogrammatic(self, n: int) -> List[str]:
            reversible_pairs = [
                ['0', '0'], ['1', '1'],
                ['6', '9'], ['8', '8'], ['9', '6']
            ]
    
            def generate_strobo_numbers(n, final_length):
                if n == 0:
                    return [""]
    
                if n == 1:
                    return ["0", "1", "8"]
    
                prev_strobo_nums = generate_strobo_numbers(n - 2, final_length)     # 길이 0 또는 1까지 들어가고 거기서 시작 (가운데부터 처리하기 위해)
                curr_strobo_nums = []
    
                for prev_strobo_num in prev_strobo_nums:
                    for pair in reversible_pairs:
                        if pair[0] != '0' or n != final_length:
                            curr_strobo_nums.append(pair[0] + prev_strobo_num + pair[1])
    
                return curr_strobo_nums
    
            return generate_strobo_numbers(n, n)
    ```
    
  - 반복문 풀이 
    ```python
    class Solution:
        def findStrobogrammatic(self, n: int) -> List[str]:
            reversible_pairs = [
                ['0', '0'], ['1', '1'], 
                ['6', '9'], ['8', '8'], ['9', '6']
            ]
    
            curr_strings_length = n % 2
            
            q = ["0", "1", "8"] if curr_strings_length == 1 else [""]
            
            while curr_strings_length < n:
                curr_strings_length += 2
                next_level = []
                
                for number in q:
                    for pair in reversible_pairs:
                        if curr_strings_length != n or pair[0] != '0':
                            next_level.append(pair[0] + number + pair[1])
                q = next_level
                
            return q
    ```