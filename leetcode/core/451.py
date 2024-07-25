class Solution:
    def frequencySort(self, s: str) -> str:
        alpha = {}

        for char in s:
            if char in alpha:
                alpha[char] += 1
            else:
                alpha[char] = 1

        keys = list(alpha.keys())

        keys.sort(key=lambda x: (-alpha[x], ord(x)))

        result = [key * alpha[key] for key in keys]

        return "".join(result)

# 시간 복잡도: O(n)      나올 수 있는 문자가 128개(아스키 코드 개수)로 고정이기 때문에 아스키코드 기준 정렬은 O(1)이라고 간주 가능
# 공간 복잡도: O(n)      나올 수 있는 문자가 128개(아스키 코드 개수)로 고정이기 때문에 딕셔너리 문자 추가는 O(1)이라고 간주 가능

# 힙큐로도 풀이 가능