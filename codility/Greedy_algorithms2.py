def solution(K, A):
    result = 0

    sumNum = 0
    for i in range(len(A)):
        sumNum += A[i]
        if sumNum >= K:
            result += 1
            sumNum = 0

    return result

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/trainingXGJ5GH-PJJ/
