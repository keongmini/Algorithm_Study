class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = collections.Counter(nums)

        for i in n.values():
            if i > 1:
                return True

        return False