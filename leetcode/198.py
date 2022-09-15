class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        rob = [0] * len(nums)
        rob[0] = nums[0]
        rob[1] = nums[1]
        rob[2] = nums[0] + nums[2]

        for i in range(3, len(nums)):
            rob[i] = max(rob[i - 2], rob[i - 3]) + nums[i]

        return max(rob)