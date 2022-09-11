class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        prev = -999

        i = 0
        while i < len(nums):
            if nums[i] == '_':
                break

            if nums[i] != prev:
                cnt += 1
                prev = nums[i]
                i += 1
            else:
                nums.remove(nums[i])
                nums.append('_')

        return cnt