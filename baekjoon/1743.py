import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

foods = {}

for _ in range(K):
    a, b = map(int, input().split())
    now = (a - 1, b - 1)
    foods[now] = True

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    q = deque([(i, j)])
    cnt = 1

    while q:
        x, y = q.popleft()

        for a, b in move:
            nx = x + a
            ny = y + b

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if (nx, ny) not in foods:
                continue

            q.append((nx, ny))
            del foods[(nx, ny)]
            cnt += 1

    return cnt


result = 0

for i in range(N):
    for j in range(M):
        if (i, j) in foods:
            del foods[(i, j)]
            result = max(result, bfs(i, j))

print(result)