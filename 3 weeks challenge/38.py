N, M = map(int, input().split())

INF = 1e9

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for a in range(1, N + 1):
    flag = False
    for b in range(1, N + 1):
        if graph[a][b] == INF and graph[b][a] == INF:
            flag = True
            break

    if not flag:
        result += 1

print(result)

