class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True

        def checkPower(num):
            if num == 3.0:
                return True
            if int(num) < 3:
                return False
            return checkPower(num / 3)

        return checkPower(n)