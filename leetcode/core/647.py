class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def check(left: int, right: int) -> int:
            cnt = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1

            return cnt

        for i in range(len(s)):     # i가 중심 역할 -> 양쪽으로 멀어지면서 비교
            even = check(i, i + 1)      # 짝수일 경우
            odd = check(i, i)           # 홀수일 경우
            result += even + odd

        return result
# 시간 복잡도 O(n^2)     최악의 경우 check가 문자열의 길이만큼 실행될 수 있음
# 공간 복잡도 O(1)       result, cnt는 상수 공간(고정된 공간)이기 때문에


# 시간 초과
class Solution:
    def check(self, string: str):
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return False

        return True

    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(1, len(s) + 1):
            for j in range(len(s)):
                if j + i > len(s):
                    break

                now_s = s[j: j + i]
                now = self.check(now_s)
                if now: result += 1

        return result
