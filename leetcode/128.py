class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            d[num] = True

        result = 0

        for num in nums:
            if num - 1 in d:
                continue

            cnt = 1

            next = num + 1
            while next in d:
                cnt += 1
                next += 1

            result = max(result, cnt)

        return result

