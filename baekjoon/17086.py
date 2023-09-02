import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

q = deque()

graph = []

for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

    for j in range(M):
        if tmp[j] == 1:
            q.append((i, j, 0))

move = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]

result = 0

while q:
    x, y, cnt = q.popleft()
    result = max(result, cnt)

    for a, b in move:
        nx = x + a
        ny = y + b

        if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] != 0:
            continue

        graph[nx][ny] = cnt + 1
        q.append((nx, ny, cnt + 1))

print(result)
