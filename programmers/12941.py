def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]

    return result