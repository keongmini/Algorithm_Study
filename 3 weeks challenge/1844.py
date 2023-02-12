from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])

    d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def bfs(i, j):
        q = deque([(i, j)])

        while q:
            x, y = q.popleft()

            for a, b in d:
                dx = x + a
                dy = y + b

                if dx < 0 or dx >= N or dy < 0 or dy >= M or maps[dx][dy] == 0:
                    continue

                if maps[dx][dy] == 1:
                    maps[dx][dy] = maps[x][y] + 1
                    q.append((dx, dy))

    bfs(0, 0)

    if maps[N - 1][M - 1] == 1:
        return -1

    return maps[N - 1][M - 1]

s = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
print(s)
