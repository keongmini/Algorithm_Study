# Timeout Error
# 시간복잡도 O(N ** 2)
def solution(A):
    cnt = 0

    for i in range(len(A)):
        if A[i] == 0:
            cnt += A[i:].count(1)

    return cnt

# 시간복잡도 O(N)
def solution(A):
    cnt = 0
    result = 0

    for i in range(len(A)):
        if A[i] == 0:
            cnt += 1
        else:
            result += cnt

    return result if result <= 1000000000 else -1

# https://app.codility.com/demo/results/trainingJUHQ3V-SBN/