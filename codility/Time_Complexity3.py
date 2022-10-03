# Timeout error
# 시간 복잡도 O(N * N)
def solution(A):
    if not A:
        return 0

    if len(A) == 1:
        return A[0]

    minNum = int(1e9)
    for i in range(1, len(A)):
        minNum = min(abs(sum(A[:i]) - sum(A[i:])), minNum)

    return minNum

# 통과
def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])

    minNum = int(1e9)
    left = 0
    right = sum(A)

    for i in range(len(A) - 1):
        left += A[i]
        right -= A[i]

        minNum = min(abs(left - right), minNum)

    return minNum

# 시간 복잡도 O(N)

# https://app.codility.com/demo/results/training68U2JM-32K/