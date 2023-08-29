def solution(n):
    result = 0

    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            result += 1

    return result