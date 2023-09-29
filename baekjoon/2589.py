# python3 통과 x / pypy 통과 o
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[char for char in input()] for _ in range(N)]


def bfs(x, y):
    visited = [[False for _ in range(M)] for i in range(N)]

    q = deque([(x, y, 0)])
    visited[x][y] = True

    now = 0

    while q:
        a, b, cnt = q.popleft()

        for ta, tb in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + ta
            nb = b + tb

            if na < 0 or na >= N or nb < 0 or nb >= M:
                continue

            if graph[na][nb] != 'L' or visited[na][nb]:
                continue

            visited[na][nb] = True
            q.append((na, nb, cnt + 1))
            now = max(now, cnt + 1)

    return now


result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)

