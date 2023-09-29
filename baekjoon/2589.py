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

# python으로 통과하기 - 참고: https://ryuwc.tistory.com/73
# 막다른 지점에서만 돌리기(양옆이나 위아래가 L이 아닐 때)
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
            # 막다른 지점 확인
            if 0 <= i - 1 < N and 0 <= i + 1 < N:       # 범위 안에 들어오는지
                if graph[i - 1][j] == 'L' and graph[i + 1][j] == 'L':       # 위아래가 육지가 아닌지
                    continue
            if 0 <= j - 1 < N and 0 <= j + 1 < M:
                if graph[i][j - 1] == 'L' and graph[i][j + 1] == 'L':       # 양옆이 육지가 아닌지
                    continue
            result = max(result, bfs(i, j))

print(result)