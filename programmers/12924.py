def solution(n):
    result = 0

    for i in range(1, n + 1):
        now = 0

        for j in range(i, n + 1):
            now += j

            if now == n:
                result += 1
                break

            if now > n:
                break

    return result