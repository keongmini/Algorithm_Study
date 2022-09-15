# 에라토스테네스의 채 
# Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        nums = [False, False] + [True] * (n - 2)

        for i in range(2, int(sqrt(n)) + 1):
            if nums[i]:
                for p in range(i * i, n, i):
                    nums[p] = False

        return sum(nums)
