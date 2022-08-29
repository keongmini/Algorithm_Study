class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1

        return cnt

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')