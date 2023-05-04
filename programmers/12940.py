def solution(n, m):
    result = []

    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            result.append(i)
            result.append(n * m / i)
            break

    return result