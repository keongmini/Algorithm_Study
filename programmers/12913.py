def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = max(land[i - 1][:j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])

# 참고. https://kimeunh3.github.io/problem%20solving/PRGRMRS_12913/ (DP)