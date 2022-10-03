def solution(X, Y, D):
    if X == Y:
        return 0

    cnt = (Y - X) // D

    if (Y - X) % D:
        cnt += 1

    return cnt

# 시간 복잡도 O(1)

# https://app.codility.com/demo/results/trainingX8U82Y-NNC/