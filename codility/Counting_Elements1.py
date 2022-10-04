def solution(X, A):
    # write your code in Python 3.6
    set_A = set()
    for idx, val in enumerate(A):
        set_A.add(val)
        if len(set_A) == X:
            return idx
    return -1

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/trainingQBKJTQ-JFE/