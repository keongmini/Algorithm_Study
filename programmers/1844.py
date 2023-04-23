from collections import deque


def solution(maps):
    N = len(maps[0])
    M = len(maps)

    visited = [[False for _ in range(N)] for _ in range(M)]
    path = [[0 for _ in range(N)] for _ in range(M)]

    q = deque()
    q.append((0, 0))
    path[0][0] = 1

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()

        for i, j in move:
            nx = x + i
            ny = y + j

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if visited[nx][ny] or maps[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            path[nx][ny] = path[x][y] + 1
            q.append((nx, ny))

    if path[M - 1][N - 1] == 0:
        return -1

    return path[M - 1][N - 1]






