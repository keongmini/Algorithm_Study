import sys

input = sys.stdin.readline

INF = 1e9

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    if graph[x][y] > z:
        graph[x][y] = z


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] >= INF:
            graph[i][j] = 0
        print(graph[i][j], end=" ")
    print()
