def solution(n):
    prev = int(n ** (1 / 2))

    if prev ** 2 == n:
        return (prev + 1) ** 2

    return -1