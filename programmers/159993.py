from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(start, end):
        q = deque()

        start.append(0)
        q.append(start)

        visited = [[False for _ in range(M)] for i in range(N)]

        while q:
            x, y, now = q.popleft()

            for a, b in move:
                nx = x + a
                ny = y + b

                if nx == end[0] and ny == end[1]:
                    return now + 1

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if maps[nx][ny] == 'X' or visited[nx][ny]:
                    continue

                q.append((nx, ny, now + 1))
                visited[nx][ny] = True

        return -1

    start = []
    lever = []
    end = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start.append(i)
                start.append(j)

            elif maps[i][j] == 'L':
                lever.append(i)
                lever.append(j)

            elif maps[i][j] == 'E':
                end.append(i)
                end.append(j)

    # S -> L
    result1 = bfs(start, lever)
    # L -> E
    result2 = bfs(lever, end)

    if result1 == -1 or result2 == -1:
        return -1

    return result1 + result2