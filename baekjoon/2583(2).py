from collections import deque


def bfs(a, b):
    q = deque()
    q.append((a, b))
    size = 1

    while q:
        x, y = q.popleft()

        for i, j in move:
            nx = x + i
            ny = y + j

            if nx < 0 or nx >= M or ny < 0 or ny >= N or graph[nx][ny] == 1:
                continue

            graph[nx][ny] = 1
            size += 1
            q.append((nx, ny))

    return size


M, N, K = map(int, input().split())
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

graph = [[0 for i in range(N)] for j in range(M)]

for _ in range(K):
    a, b, x, y = map(int, input().split())

    for i in range(a, x):
        for j in range(b, y):
            graph[j][i] = 1

result = 0
size = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result += 1
            size.append(bfs(i, j))

size.sort()

print(result)
print(*size)