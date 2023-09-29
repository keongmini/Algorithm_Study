import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[False for _ in range(N)] for i in range(M)]

for k in range(K):
    si, sj, ei, ej = list(map(int, input().split()))
    for i in range(si, ei):
        for j in range(sj, ej):
            graph[j][i] = True

graph.reverse()


def bfs(x, y):
    q = deque([(x, y)])
    cnt = 0

    while q:
        a, b = q.popleft()
        cnt += 1

        for ta, tb in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + ta
            nb = b + tb

            if na < 0 or na >= M or nb < 0 or nb >= N or graph[na][nb]:
                continue

            q.append((na, nb))
            graph[na][nb] = True

    return cnt


result = 0
area = []

for i in range(M):
    for j in range(N):
        if not graph[i][j]:
            graph[i][j] = True
            now = bfs(i, j)
            area.append(now)
            result += 1

area.sort()

print(result)
for a in area:
    print(a, end=" ")