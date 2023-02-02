import heapq
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

distance = [1e9 for _ in range(N + 1)]
distance[0] = 0

q = []

heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    d, n = heapq.heappop(q)

    if distance[n] < d:
        continue

    for k in graph[n]:
        if d + 1 < distance[k]:
            distance[k] = d + 1
            heapq.heappush(q, (d + 1, k))

result = max(distance)
index = N + 1
cnt = 0

for i in range(len(distance)):
    if distance[i] == result:
        index = min(index, i)
        cnt += 1

print(index, result, cnt)