import heapq
from collections import defaultdict

N, M = map(int, input().split())

INF = 1e9

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF for _ in range(N + 1)]

def dijkstra(d, i):
    q = []

    heapq.heappush(q, (d, i))
    distance[i] = d

    while q:
        now, a = heapq.heappop(q)

        if distance[a] < now:
            continue

        for b in graph[a]:
            if now + 1 < distance[b]:
                distance[b] = now + 1
                heapq.heappush(q, (now + 1, b))

dijkstra(0, 1)

result = max(distance[1:])
index = N + 1
cnt = 0

for i in range(len(distance)):
    if distance[i] == result:
        index = min(index, i)
        cnt += 1

print(index, result, cnt)



