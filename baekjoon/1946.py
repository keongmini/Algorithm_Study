import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    heap = []

    for _ in range(N):
        a, b = map(int, input().split())
        heapq.heappush(heap, (a, b))

    result = 1

    check = heapq.heappop(heap)[1]

    while heap:
        i, now = heapq.heappop(heap)

        if now < check:
            result += 1
            check = now

    print(result)

