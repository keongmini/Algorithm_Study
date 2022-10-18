# leetcode 3. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (medium)

* 문제 해설 : 반복되는 문자 없이 이어지는 문자열 중 가장 긴 문자열의 길이 구하기

  example1. 
  ```text
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.
  ```
  
  example2. 
  ```text
  Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.
  ```
    
  example3.
  ```text
  Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.
  ```
  
  제약조건.
  ```text
  0 <= s.length <= 5 * 10^4
  s consists of English letters, digits, symbols and spaces.
  ```

* 문제 접근 방법

  1. 총 3개의 변수 선언 :   
    중복 확인을 위해 문자를 저장할 set 변수 a    
    이어지는 문자열을 만들 변수 b  
    최대 길이(결과값)을 저장할 변수 c
  1. 문자열 반복문 돌면서 문자 하나씩 처리
  1. a에 문자가 없으면 a에 저장, b에 연결
  1. a에 문자가 있을 경우 b의 길이를 c의 값과 비교 - 더 큰 값 저장
  1. 문자열 전체 확인 후 c 반환 
  
  **시간복잡도: O(N)**  
  **완전탐색(브루트 포스)**
  
  ```python
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxNum = 0
        now = ''
        set_now = set()
        for char in s:
            if set_now and char in set_now:
                for i in range(len(now)):
                    if now[i] == char:
                        now = now[i+1:]
                        break
            set_now.add(char)
            now += char
            maxNum = max(maxNum, len(now))
                
        return maxNum
    ```
*  다른 접근 방법

    **Sliding Window**   
    https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
    
  


* 참고할 내용
    - set이 list보다 탐색속도가 빠름 [Time complexity of python set operations](https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations)
  

  