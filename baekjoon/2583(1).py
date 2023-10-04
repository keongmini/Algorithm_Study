import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[False for _ in range(M)] for i in range(N)]

for _ in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            graph[i][j] = True


def bfs(x, y):
    q = deque([(x, y)])
    now = 1

    while q:
        a, b = q.popleft()

        for ta, tb in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + ta
            nb = b + tb

            if na < 0 or na >= N or nb < 0 or nb >= M or graph[na][nb]:
                continue

            graph[na][nb] = True
            now += 1
            q.append((na, nb))

    return now


result = []
for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            graph[i][j] = True
            now = bfs(i, j)
            result.append(now)

result.sort()

print(len(result))
for r in result:
    print(r, end=" ")
