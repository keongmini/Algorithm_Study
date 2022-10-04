# Wrong Answer
def solution(A, B, K):
    if B < K:
        if A == 0 or B == 0:
            return 1
        return 0

    if A == B:
        return 1 if A % K == 0 else 0

    result = (B - A + 1) // K

    if K > A:
        return result + 1
    else:
        return result

# 시간복잡도 O(1)
def solution(A, B, K):
    A1, A2 = divmod(A, K)
    B1, B2 = divmod(B, K)

    return B1 - A1 + 1 if A2 == 0 else B1 - A1

# https://app.codility.com/demo/results/trainingHH4S74-9KX/