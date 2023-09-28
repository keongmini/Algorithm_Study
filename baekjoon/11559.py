import sys
from collections import deque

input = sys.stdin.readline

graph = [[char for char in input()] for _ in range(12)]


def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    cnt = 1

    graph_list = []                         # 모여 있는 뿌요의 위치

    while q:
        a, b = q.popleft()
        graph_list.append((a, b))

        for ta, tb in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + ta
            nb = b + tb

            if na < 0 or na >= 12 or nb < 0 or nb >= 6:
                continue

            if graph[na][nb] != color or visited[na][nb]:
                continue

            visited[na][nb] = True
            cnt += 1
            q.append((na, nb))

    if cnt >= 4:                                            # 4개 이상 모였기 때문에 없애기 위해서 pyuo list에 담아줌 - 이 시점에서 없애게 되면 동시에 터져야 하는 뿌요 그룹에 영향을 줄 수 도 있음
        graph_list.sort(key = lambda x: (x[1], x[0]))       # y축 기준으로 먼저 정렬
        for gx, gy in graph_list:
            puyo_list.append((gx, gy))
    else:
        for gx, gy in graph_list:
            visited[gx][gy] = False                         # 다시 돌려놓기


result = 0
while True:
    visited = [[False for _ in range(6)] for i in range(12)]
    puyo_list = []                                          # 없애줄 뿌요 위치

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, graph[i][j])

    if not puyo_list:
        break

    for px, py in puyo_list:
        for i in range(px, 0, -1):
            graph[i][py] = graph[i - 1][py]                 # 없어진 위치부터 한칸씩 내려주기
        graph[0][py] = '.'                                  # 맨 끝칸은 값이 없음

    result += 1

print(result)