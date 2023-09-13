import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0 for i in range(N)] for j in range(M)]

    for k in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1


    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            a, b = q.popleft()

            for u, v in move:
                na = a + u
                nb = b + v

                if na < 0 or na >= M or nb < 0 or nb >= N:
                    continue

                if graph[na][nb] != 1:
                    continue

                q.append((na, nb))
                graph[na][nb] = -1


    result = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)
