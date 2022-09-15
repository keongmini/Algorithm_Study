# 내장함수 사용
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        return haystack.index(needle)

# 내장함수 없이 풀이(leetcode discussion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i + length] == needle:
                    return i

        return -1