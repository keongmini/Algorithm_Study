import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

result = [1e9 for _ in range(N + 1)]


def dijkstra(x):
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        path, now = heapq.heappop(heap)

        if result[now] < path:
            continue

        for n, cnt in graph[now]:
            cost = path + cnt

            if cost < result[n]:
                result[n] = cost
                heapq.heappush(heap, (cost, n))


dijkstra(start)
print(result[end])