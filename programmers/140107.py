import math


def solution(k, d):
    result = 0

    for i in range(0, d + 1, k):
        if i ** 2 > d ** 2:
            break

        now = d ** 2 - i ** 2

        result += int(math.sqrt(now) // k) + 1

    return result