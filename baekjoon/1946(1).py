import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    heap = []

    for _ in range(N):
        a, b = map(int, input().split())
        heapq.heappush(heap, (a, b))

    check = 100001
    result = 0

    while heap:
        a, b = heapq.heappop(heap)

        if b < check:
            check = b
            result += 1

    print(result)