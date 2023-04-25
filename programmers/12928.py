def solution(n):
    result = 0

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            if i ** 2 == n:
                result += i
            else:
                result += i
                result += n // i

    return result