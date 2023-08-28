# 통과
def solution(n):
    result = 0

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            result += 1
            n -= 1

    return result


# dp - 시간초과
def solution(n):
    result = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        if i % 2 == 0:
            result[i] = min(result[i], result[i // 2])
        else:
            result[i] = min(result[i], result[i - 1] + 1)

    return result[n]