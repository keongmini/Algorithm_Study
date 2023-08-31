from collections import deque

N, M = map(int, input().split())

graph = [[int(s) for s in input()] for _ in range(N)]

q = deque()
q.append((0, 0, 1))

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    x, y, cnt = q.popleft()

    for a, b in move:
        nx = x + a
        ny = y + b

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] != 1:
            continue

        graph[nx][ny] = cnt + 1
        q.append((nx, ny, graph[nx][ny]))

print(graph[N - 1][M - 1])