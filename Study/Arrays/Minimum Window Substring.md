# leetcode 76. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (hard)

* 문제 해설 : t의 값이 모두 포함된 연속되는 문장을 s에서 찾되 길이가 가장 짧은 문장 찾기

  example 1. 
  ```text
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    ```
  
  example 2.
  ```text
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    ```
  
  example 3.
  ```text
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.
    ```
  
  제약조건.
  ```text
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.
    ```

* 문제 접근 방법  
  s에서 t에 해당하는 문자의 개수를 저장해놓고 슬라이딩 원도우를 사용하여 풀고자 함  
  풀지 못한 이유:  
    - t의 각 문자가 고유한 값이 아닐 수 있음, 해당 문자의 갯수도 확인해야함 - 해결 x
    - O(M + N)의 효율적인 풀이 방법 생각 못함
    
* Solution 풀이
  - 슬라이딩 윈도우  
    참고. 파이썬 알고리즘 인터뷰
    
    1. t에 있는 문자의 각 개수 저장한 딕셔너리, t의 길이 저장한 변수 각 선언
    1. s를 반복문으로 돌면서 각 자리수의 개수 1개씩 빼주기, t에 있는 값(딕셔너리에 값이 1 이상)이면 t의 길이 - 1
    1. 길이가 0이 되었을 때 left부터 right까지 최소 길이 계속 업데이트
    
    **시간복잡도 O(s + t)**
    > The time complexity includes the length of T because you need to iterate through T in order to count the frequencies in which the characters appear in T. Since that's not part of a nested loop, you add the length of T to the time complexity. This step occurs when you're constructing the hash map for the T char frequencies.  
      So a more "accurate" way to portray the time complexity would be:
    O(2S + T)
    which gets simplified to O(S+T)  
    참고. leetcode solution comment
    
    ```python
    class Solution:
        def minWindow(self, s: str, t: str) -> str:
            need = collections.Counter(t)
            missing = len(t)
            left = start = end = 0
            
            for right, char in enumerate(s, 1):     # 주의! 1부터 시작
                missing -= need[char] > 0       # 찾아야하는 값(t에 있는 값) 모두 찾았는지 확인용
                need[char] -= 1
                
                if missing == 0:        # t에 있는 값 모두 찾음
                    while left < right and need[s[left]] < 0:       # t에 있는 값부터 시작할 수 있도록 left 땡기기 (t에 없는 값은 딕셔너리 value가 0보다 작기 때문)
                        need[s[left]] += 1
                        left += 1
                    
                    if not end or right - left <= end - start:      # 이전에 찾는 연속된 문자열의 길이 보다 작을 경우에 업데이트
                        start, end = left, right
                        need[s[left]] += 1
                        missing += 1
                        left += 1
            
            return s[start:end]
    ```
    
 