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


# ---

from collections import deque

class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)

        minus = False
        if string[0] == '-':            # 음수인지 확인
            minus = True
            string = string[1:]

        result = deque()
        for char in string:
            result.appendleft(char)

        answer = int(''.join(result))

        if answer > 2 ** 31 - 1 or answer < -2 ** 31:           # 문제 조건
            return 0

        return answer if minus == False else (-1) * answer


