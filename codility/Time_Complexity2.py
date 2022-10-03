def solution(A):
    if not A:
        return 1

    A.sort()

    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1

    return A[-1] + 1

# 시간 복잡도 O(N) or O(N * log(N))