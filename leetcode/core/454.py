from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        nums = defaultdict(int)         # hashmap
        result = 0

        for i in nums1:
            for j in nums2:
                now = i + j
                nums[now] += 1

        for i in nums3:
            for j in nums4:
                now = 0 - (i + j)           # i + j 인 값이 key 이기 때문에 nums3, nums4의 값 중 더해서 0이 되는 값 찾기 (대칭구조라고 생각)
                result += nums[now]

        return result

# 시간 복잡도: O(n^2)
# 공간 복잡도: O(n^2) 두개를 더한 값과 그 값의 등장횟수

    # 재귀: O(n^4) 시간초과
    # def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
    #     result = 0
    #     nums = [nums1, nums2, nums3, nums4]
    #
    #     def check(num, i):
    #         if i >= 4:
    #             if num == 0:
    #                 return 1
    #             return 0
    #
    #         cnt = 0
    #         for n in nums[i]:
    #             cnt += check(num + n, i + 1)
    #
    #         return cnt
    #
    #     for num in nums1:
    #         result += check(num, 1)
    #
    #     return result
