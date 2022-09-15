class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        store_nums = [-10001] * len(nums)
        store_nums[0] = nums[0]

        for i in range(1, len(nums)):
            store_nums[i] = max(store_nums[i - 1] + nums[i], nums[i - 1] + nums[i])

        store_nums[-1] = max(nums[-1], store_nums[-1])

        return max(max(store_nums), max(nums))