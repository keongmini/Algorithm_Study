import math


def solution(n, k):
    result = []

    nums = [i + 1 for i in range(n)]

    while n != 0:
        f = math.factorial(n - 1)
        q = k // f
        k = k % f

        if k == 0:
            now = nums.pop(q - 1)
        else:
            now = nums.pop(q)

        result.append(now)
        n -= 1

    return result


# 참고. https://velog.io/@hsjunior1/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95Python
# itertools permutation 이용시 시간초과