import sys
import collections

input = sys.stdin.readline

M, N, H = map(int, input().split())

q = collections.deque()

graph = []

for i in range(H):
    now = []
    for j in range(N):
        tmp = list(map(int, input().split()))
        now.append(tmp)

        for k in range(M):
            if tmp[k] == 1:
                q.append((j, k, i, 0))

    graph.append(now)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

result = 0

while q:
    x, y, z, path = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
            continue

        if graph[nz][nx][ny] == 1 or graph[nz][nx][ny] == -1:
            continue

        graph[nz][nx][ny] = 1
        q.append((nx, ny, nz, path + 1))

    result = max(result, path)

for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 0:
                print(-1)
                exit(0)

print(result)


