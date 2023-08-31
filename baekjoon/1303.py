import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[s for s in input()] for _ in range(M)]
visited = [[False for _ in range(N)] for i in range(M)]

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y, num):
    q = deque()
    q.append((x, y))
    cnt = 1

    while q:
        a, b = q.popleft()

        for u, v in move:
            na = a + u
            nb = b + v

            if na < 0 or na >= M or nb < 0 or nb >= N:
                continue

            if visited[na][nb] or graph[na][nb] != num:
                continue

            q.append((na, nb))
            visited[na][nb] = True
            cnt += 1

    return cnt


result = {'B': 0, 'W': 0}

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            now = bfs(i, j, graph[i][j])
            result[graph[i][j]] += (now ** 2)

print(result['W'], result['B'])