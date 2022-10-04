def solution(A):
    A.sort()

    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0

# 시간 복잡도 O(N*log(N))

# https://app.codility.com/demo/results/trainingM9TVNN-QXY/