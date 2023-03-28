import heapq
from collections import defaultdict


def solution(k, tangerine):
    nums = defaultdict(int)

    for t in tangerine:
        nums[t] += 1

    fruit = []
    for num in nums:
        heapq.heappush(fruit, nums[num])

    n = len(tangerine)

    result = 0
    while n > k:
        num = heapq.heappop(fruit)

        n -= num

        if n < k:
            result += 1

    result += len(fruit)

    return result

