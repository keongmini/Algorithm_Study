import sys
from collections import deque

input = sys.stdin.readline

graph = [[char for char in input()] for _ in range(12)]


def bfs(x, y, color):
    q = deque()
    q.append((x, y))

    graph_list = []

    while q:
        a, b = q.popleft()
        cnt = 1
        graph_list.append((a, b))

        for ta, tb in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + ta
            nb = b + tb

            if na < 0 or na >= 12 or nb < 0 or nb >= 6:
                continue

            if graph[na][nb] != color or visited[na][nb] == False:
                continue

            visited[na][nb] = True
            cnt += 1

    if cnt >= 4:
        graph_list.sort(key = lambda x: (x[1], x[0]))
        for gx, gy in graph_list:
            puyo_list.append((gx, gy))


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

    for px, py in puyo_list:
        for i in range(px, 0, -1):
            graph[i][py] = graph[i - 1][py]
        graph[0][py] = '.'

    result += 1

print(result)