import collections


def solution(A):
    visited = [-1 for _ in range(max(A) + 1)]

    nums = collections.defaultdict(int)
    for a in A:
        nums[a] += 1

    result = []

    for a in A:
        divisor = 0

        if visited[a] != -1:
            result.append(visited[a])
            continue

        for i in range(1, int(a ** 0.5) + 1):
            if a % i == 0:
                divisor += nums[i]

                if a // i != i:
                    divisor += nums[a // i]

        result.append(len(A) - divisor)
        visited[a] = len(A) - divisor

    return result

# 시간복잡도 O(N * log(N))

# https://app.codility.com/demo/results/trainingGS28TM-TC7/ 