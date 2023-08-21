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

distance = [1e9 for _ in range(N + 1)]


def dijkstra(x):
    q = []

    heapq.heappush(q, (0, x))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_step, next_dist in graph[now]:
            cost = dist + next_dist

            if cost < distance[next_step]:
                distance[next_step] = cost
                heapq.heappush(q, (cost, next_step))


dijkstra(start)

print(distance[end])
