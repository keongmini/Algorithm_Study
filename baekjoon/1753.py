import collections
import heapq
import sys

input = sys.stdin.readline          # 없으면 시초 발생 

def dij(start, visited):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:
        now = heapq.heappop(q)

        if visited[now[1]] < now[0]:
            continue

        for v, w in graph[now[1]]:
            cost = now[0] + w
            if cost < visited[v]:
                visited[v] = cost
                heapq.heappush(q, (cost, v))

N, M = map(int, input().split())

K = int(input())

graph = collections.defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

visited = [1e9 for _ in range(N + 1)]

dij(K, visited)

for i in range(1, N + 1):
    if visited[i] == 1e9:
        print('INF')
    else:
        print(visited[i])

