# 타임아웃
class Solution:
    def climbStairs(self, n: int) -> int:
        def step(now, n, cnt):
            if now == n:
                return 1

            if now > n:
                return 0

            return cnt + step(now + 1, n, cnt) + step(now + 2, n, cnt)

        return step(0, n, 0)

# 메모이제이션 이용 - 통과
class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [0] * (n + 1)

        if n <= 2:
            return n

        nums[1] = 1
        nums[2] = 2
        for i in range(3, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]

        return nums[n]