import sys
import heapq

w, t = map(int, input().split())

heap = []

for _ in range(t):
    m, p = map(int, input().split())
    heapq.heappush(heap, (-p, m))

result = 0

while w > 0 and heap:

    p, m = heapq.heappop(heap)

    p = p * (-1)

    if m >= w:
        result += w * p
        break
    else:
        result += m * p
        w -= m

print(result)
