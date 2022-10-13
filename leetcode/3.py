# 잘못된 풀이: 값이 하나만 들어올 경우 counts에 값이 없음
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        if not len(s):
            return 0

        counts = []
        freqs = []

        cnt = 0
        for char in s:
            if char not in freqs:
                freqs.append(char)
                cnt += 1
            else:
                del freqs[:]
                freqs.append(char)
                counts.append(cnt)
                cnt = 1

        return max(counts)

# 정답 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length

# 다시 풀어봄

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxNum = 0
        now = ''
        set_now = set()
        for char in s:
            if set_now and char in set_now:
                for i in range(len(now)):
                    if now[i] == char:
                        now = now[i + 1:]
                        break
            set_now.add(char)
            now += char
            maxNum = max(maxNum, len(now))

        return maxNum