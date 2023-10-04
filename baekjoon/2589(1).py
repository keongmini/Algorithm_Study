import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[char for char in input()] for _ in range(N)]


def bfs(x, y):
    q = deque([(x, y, 0)])
    visited = [[False for _ in range(M)] for i in range(N)]
    visited[x][y] = True

    answer = 0

    while q:
        a, b, cnt = q.popleft()

        for ta, tb in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + ta
            nb = b + tb

            if na < 0 or na >= N or nb < 0 or nb >= M:
                continue

            if graph[na][nb] != 'L' or visited[na][nb]:
                continue

            q.append((na, nb, cnt + 1))
            answer = max(answer, cnt + 1)
            visited[na][nb] = True

    return answer


result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            if 0 <= i - 1 < N and 0 <= i + 1 < N:
                if graph[i - 1][j] == 'L' and graph[i + 1][j] == 'L':           # and!!! - 둘다 해당 될 때 막다른 길이 아닌거니까
                    continue

            if 0 <= j - 1 < M and 0 <= j + 1 < M:
                if graph[i][j - 1] == 'L' and graph[i][j + 1] == 'L':
                    continue

            result = max(result, bfs(i, j))

print(result)