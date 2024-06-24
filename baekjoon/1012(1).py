from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 0:
                continue

            graph[nx][ny] = 0
            q.append((nx, ny))


T = int(input())
move = [(1, 0), (0, 1), (0, -1), (-1, 0)]

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for i in range(M)] for j in range(N)]

    for k in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)
