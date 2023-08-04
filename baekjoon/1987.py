# 시간 초과
import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[s for s in input()] for _ in range(R)]

visited = {}

result = 1

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y, cnt):
    global result

    result = max(result, cnt)

    visited[graph[x][y]] = True

    for a, b in move:
        nx = x + a
        ny = y + b

        if nx < 0 or nx >= R or ny < 0 or ny >= C or graph[nx][ny] in visited:
            continue

        dfs(nx, ny, cnt + 1)

    del visited[graph[x][y]]


dfs(0, 0, 1)

print(result)