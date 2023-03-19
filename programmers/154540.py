from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    graph = []
    visited = []

    for m in maps:
        tmp = []
        for char in m:
            if char.isdigit():
                tmp.append(int(char))
            else:
                tmp.append(char)
        graph.append(tmp)
        visited.append([False for _ in range(len(m))])

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(x, y):
        q = deque([(x, y)])
        now = graph[x][y]

        while q:
            a, b = q.popleft()

            for dx, dy in move:
                nx = a + dx
                ny = b + dy

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                if graph[nx][ny] == 'X' or visited[nx][ny]:
                    continue

                now += graph[nx][ny]
                visited[nx][ny] = True
                q.append((nx, ny))

        return now

    result = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if visited[i][j]:
                continue

            if graph[i][j] == 'X':
                continue

            visited[i][j] = True
            result.append(bfs(i, j))

    if not result:
        result.append(-1)

    result.sort()

    return result