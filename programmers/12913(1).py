def solution(land):
    N = len(land)
    M = len(land[0])

    for i in range(1, N):
        for j in range(M):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[-1])
