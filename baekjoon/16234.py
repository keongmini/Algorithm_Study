from collections import deque
import math
import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    new = list(map(int, input().split()))
    graph.append(new)

move = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(a, b, visited):
    q = deque()
    q.append((graph[a][b], a, b))

    visited[a][b] = True

    sumNum = graph[a][b]
    cnt = 1
    save = [(a, b)]
    moved = False

    while q:
        people, i, j = q.popleft()

        for x, y in move:
            dx = x + i
            dy = y + j

            if dx < 0 or dx >= N or dy < 0 or dy >= N or visited[dx][dy]:
                continue

            if abs(people - graph[dx][dy]) < L or abs(people - graph[dx][dy]) > R:
                continue

            sumNum += graph[dx][dy]
            cnt += 1
            q.append((graph[dx][dy], dx, dy))
            save.append((dx, dy))
            visited[dx][dy] = True
            moved = True

    chage = math.trunc(sumNum / cnt)

    for x, y in save:
        graph[x][y] = chage

    return moved

result = 0
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if not visited[a][b]:
                if bfs(a, b, visited):
                    flag = True

    if not flag:
        break
    else:
        result += 1

print(result)
