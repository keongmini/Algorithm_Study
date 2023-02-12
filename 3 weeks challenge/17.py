from collections import deque

N, K = map(int, input().split())
graph = []
nums = []
for i in range(N):
    new = list(map(int, input().split()))
    graph.append(new)

    for j in range(len(new)):
        if new[j] != 0:
            nums.append((new[j], i, j, 0))

S, X, Y = map(int, input().split())

nums.sort()
q = deque(nums)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    now, x, y, time = q.popleft()

    if time == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] != 0:
            continue

        graph[nx][ny] = now
        q.append((graph[nx][ny], nx, ny, time + 1))

print(graph[X - 1][Y - 1])