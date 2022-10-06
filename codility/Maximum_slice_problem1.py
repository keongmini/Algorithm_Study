def solution(A):
    if not A:
        return 0

    profit = 0
    minNum = A[0]

    for i in range(1, len(A)):
        if A[i] < minNum:
            minNum = A[i]
        else:
            profit = max(profit, A[i] - minNum)

    return profit

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/training83K79V-V5C/