def solution(A):
    result = [A[0]]

    for i in range(1, len(A)):
        result.append(max(result[i - 1] + A[i], A[i - 1] + A[i]))

    if max(result) > max(A):
        return max(result)

    return max(A)

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/trainingVQG4ZW-P39/