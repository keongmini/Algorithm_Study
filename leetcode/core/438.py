from collections import defaultdict

class Solution:
    # 슬라이딩 윈도우
    def findAnagrams(self, s: str, p: str):
        nums = defaultdict(int)     # value = 1 앞쪽 기준으로 있음 -1 뒷쪽 기준으로 있음
        S = len(s)
        P = len(p)

        if P > S:
            return []

        for char in p:
            nums[char] += 1

        # 윈도우 뒷쪽 가장 끝으로 보내기
        for i in range(P - 1):          # P-1인 이유) 마지막 자리는 다음 반복문에서 처리 예정 (현재 유효한 문자 길이는 P-1임)
            if s[i] in nums:            # 뒷쪽으로 이동하면서 현재 있는 값 빼주기 (0일 때 만족 하는 값이 됨)
                nums[s[i]] -= 1

        result = []
        for i in range(-1, S - P + 1):
            if i > -1 and s[i] in nums:     # 앞쪽 이동
                nums[s[i]] += 1
            if i + P < S and s[i + P] in nums:      # 뒤쪽 이동
                nums[s[i + P]] -= 1

            if all(v == 0 for v in nums.values()):      # 전체 값이 0인지 확인
                result.append(i + 1)

        return result
    # 시간 복잡도 O(S)
    # 공간 복잡도 O(1)       딕셔너리에 저장되는 최대개수 26 (알파벳 소문자만 다루기 때문에)
    # 공간 복잡도 O(S)로 보기도 함 (최악의 경우, 모든 인덱스가 다 저장될 때 S - P의 길이만큼 저장할 수 있음)
    # Runtime 131ms

    # # 통과 - 효율성 떨어짐 Runtime 8056ms
    # # 시간 복잡도 O(n * mlog(m))  m = 길이
    # # 공간 복잡도 O(n)
    # def findAnagrams(self, s: str, p: str):
    #     now = []
    #     length = len(p)
    #     P = "".join(sorted(p))
    #
    #     result = []
    #     for i, char in enumerate(s):
    #         if len(now) < length:
    #             now.append(char)
    #         else:
    #             now = now[1:]
    #             now.append(char)
    #
    #         if len(now) == length and "".join(sorted(now)) == P:
    #             result.append(i - length + 1)
    #
    #     return result
