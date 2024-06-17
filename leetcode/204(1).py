# 시간초과
class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False

            return True

        result = 0

        for i in range(2, n):
            if isPrime(i):
                result += 1
        
        return result


# 통과
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        nums = [True for _ in range(n)]
        nums[0] = False
        nums[1] = False

        for i in range(2, int(sqrt(n)) + 1):
            if nums[i]:
                for p in range(i * i, n, i):
                    nums[p] = False

        return sum(nums)
