from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for z in range(h)]

    result = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for a, b in move:
                        nx = x + a
                        ny = y + b

                        if nx < 0 or nx >= h or ny < 0 or ny >= w:
                            continue

                        if graph[nx][ny] == 0 or visited[nx][ny]:
                            continue

                        visited[nx][ny] = True
                        q.append((nx, ny))

                result += 1

    print(result)


