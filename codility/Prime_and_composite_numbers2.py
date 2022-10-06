import math


def solution(N):
    minNum = (int(1e9) + 2) * 2
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            answer = (i + (N // i)) * 2
            minNum = min(minNum, answer)

    return minNum

# 시간복잡도 O(sqrt(N))

# https://app.codility.com/demo/results/trainingG853VX-WJJ/