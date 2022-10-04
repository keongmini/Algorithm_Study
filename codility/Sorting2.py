def solution(A):
    A.sort(reverse = True)

    return max(A[0] * A[1] * A[2], A[0] * A[-1] * A[-2])

# O(N * log(N))

# https://app.codility.com/demo/results/training789C7G-CRW/