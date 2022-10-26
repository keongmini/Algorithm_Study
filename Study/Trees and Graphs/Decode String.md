# leetcode 394. [Decode String](https://leetcode.com/problems/decode-string/) (medium)

* 문제 해설 : 중괄호안에 있는 문자열을 중괄호 앞에 있는 숫자만큼 반복하는 문자열 출력  
 
  example 1. 
  ```text
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
    ```
  
  example 2.
  ```text
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    ```
  
  example 3.
  ```text
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    ```
  
  제약조건.
  ```text
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
    ```
* 문제 접근 방법  
  stack을 두개 선언해서 모든 문자열 관리, 괄호만 관리 하는 stack을 사용하려고 함  
  유효한 괄호만 들어오기 때문에 ']' 가 들어오면 모든 문자를 관리하는 stack에서 '['가 나올 때까지 문자열을 다 추출하고 숫자만큼 반복하여 계속 문자열에 저장  
  주요 케이스 처리x
  
  * 고려하지 못한 테스트케이스 
    - [100[leetcode]] : 숫자가 2자리수 이상일 때
    - [ab3[cd]ef] : 반복과 상관없는 문자도 있는 경우

* Solution 풀이
  - stack  
    참고. [discussion python solution](https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack)
    
    숫자 저장, 문자 저장할 변수 각각 선언하여 현재까지 진행상황 관리, stack에는 괄호 전 완성된 문자와 숫자 저장 용도
    
    **시간복잡도 O(N^2)** 
    > I also think O(n^2) because we are looping through O(n) but string concatenation in python is O(n) hence O(n^2)
    
    ```python
    class Solution:
        def decodeString(self, s: str) -> str:
            stack = []
            current_num = ''
            current_string = ''
            
            for char in s:
                if char.isdigit():
                    current_num += char
                
                elif char == '[':
                    stack.append(current_string)        # 현재까지 문자열 저장
                    stack.append(current_num)           # 반복할 숫자 저장 
                    current_string = ''                 # 초기화 - 괄호열리는 순간 다시 시작
                    current_num = ''
                    
                elif char == ']':
                    num = stack.pop()
                    if num:
                        num = int(num)
                    
                    prev_string = stack.pop()
                    current_string = prev_string + num * current_string     # 이전 구현된 문자열과 합해서 다시 저장
                
                else:
                    current_string += char
                
            return current_string
    ```
    
* 알아둘 구현 방법
  ```python
  current_num = 0
  
  for char in s:
    if char.isdigit():
      current_num = current_num * 10 + int(char)
    ```
  
  문자열에 숫자 연결하듯이 각 자리수 구현 가능