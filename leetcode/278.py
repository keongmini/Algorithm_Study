# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while right - left > 1:
            mid = (left + right + 1) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        return right