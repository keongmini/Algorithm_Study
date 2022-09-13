class Solution:
    def firstUniqChar(self, s: str) -> int:
        nums = collections.Counter(s)

        for i in s:
            if nums[i] == 1:
                return s.index(i)

        return -1
