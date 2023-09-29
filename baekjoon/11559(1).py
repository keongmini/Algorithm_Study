import sys
from collections import deque

input = sys.stdin.readline

graph = [[char for char in input()] for _ in range(12)]


def bfs(x, y, now):
    q = deque([(x, y)])
    cnt = 1
    now_list = []

    while q:
        a, b = q.popleft()
        now_list.append((a, b))

        for ta, tb in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + ta
            nb = b + tb

            if na < 0 or na >= 12 or nb < 0 or nb >= 6:
                continue

            if graph[na][nb] != now or visited[na][nb]:
                continue

            visited[na][nb] = True
            q.append((na, nb))
            cnt += 1

    if cnt >= 4:
        now_list.sort(key=lambda x: (x[1], x[0]))
        for l in now_list:
            puyo_list.append(l)
    else:
        for a, b in now_list:
            visited[a][b] = False


result = 0
while True:
    visited = [[False for _ in range(6)] for i in range(12)]
    puyo_list = []

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, graph[i][j])

    if not puyo_list:
        break

    for pa, pb in puyo_list:
        for i in range(pa, 0, -1):
            graph[i][pb] = graph[i - 1][pb]
        graph[0][pb] = '.'

    result += 1

print(result)