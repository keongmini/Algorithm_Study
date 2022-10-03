import collections

def solution(A, K):
    if not A:
        return A

    nums = collections.deque(A)

    for _ in range(K):
        nums.appendleft(nums.pop())

    result = list(nums)

    return result

# https://app.codility.com/demo/results/trainingVJRMYK-Q6N/