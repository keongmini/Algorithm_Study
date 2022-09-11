class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        op = ''
        if x[0] == '-':
            op = x[0]
            x = x[1:]

        for i in range(len(x) // 2):
            x[i], x[-1 - i] = x[-1 - i], x[i]

        result = op + str(int(''.join(x)))

        if int(result) > 2 ** 31 - 1 or int(result) < -2 ** 31:
            return 0

        return result