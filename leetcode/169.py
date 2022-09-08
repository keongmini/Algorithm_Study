# 풀이 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = collections.Counter(nums)
        length = len(nums) // 2

        for i in list(set(nums)):
            if data[i] > length:
                return i
