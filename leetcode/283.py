class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(len(nums)):
            if 0 in nums:
                nums.remove(0)
                nums.append(0)
            else:
                return