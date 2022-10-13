def solution(A, B):
    if not A or not B:
        return 0

    result = 1
    prev = B[0]
    for i in range(1, len(A)):
        if A[i] > prev:
            result += 1
            prev = B[i]

    return result

# 시간복잡도 O(N)
# https://app.codility.com/demo/results/trainingAYRUB8-55Z/
