def solution(A):
    tmp = list(set(A))

    if len(tmp) != len(A):
        return 0

    if len(A) != max(A):
        return 0

    return 1

# 시간 복잡도 O(N) or O(N * log(N))

# https://app.codility.com/demo/results/trainingMFGDEJ-JP8/