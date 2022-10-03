def solution(A):
    A.sort()

    now = A[0]
    cnt = 1
    for i in range(1, len(A)):
        if A[i] == now:
            cnt += 1
        else:
            if not cnt % 2:
                now = A[i]
                cnt = 1
            else:
                return now

    return now

# 시간 복잡도 O(N) or O(N*log(N))

# https://app.codility.com/demo/results/trainingPVNRJR-SPY/