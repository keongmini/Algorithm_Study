class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x

        start = 1
        end = x
        while start < end - 1:
            mid = (start + end) // 2
            now = mid ** 2

            if now == x:
                return mid
            elif now < x:
                start = mid
            elif now > x:
                end = mid

        return start

# 딱 떨어지는 n 제곱근이 아니라 제곱근에 가장 가까운 수를 구해야 함