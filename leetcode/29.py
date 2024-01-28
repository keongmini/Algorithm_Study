class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        now = int(abs(dividend) / abs(divisor))

        sign = 1 if dividend * divisor > 0 else -1

        result = now * sign

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -(2 ** 31):
            return -(2 ** 31)

        return result