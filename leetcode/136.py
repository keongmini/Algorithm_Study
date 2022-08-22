# 파이썬 풀이
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = collections.Counter(nums)

        for i in set(nums):
            if numbers[i] == 1:
                return i

# 비트 조작
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result