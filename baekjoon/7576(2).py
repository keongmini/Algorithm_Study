import collections

M, N = map(int, input().split())

q = collections.deque()

graph = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            q.append((i, j, 0))
    graph.append(tmp)

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = 0

while q:
    x, y, path = q.popleft()

    for a, b in move:
        nx = x + a
        ny = y + b

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] == 1 or graph[nx][ny] == -1:
            continue

        q.append((nx, ny, path + 1))
        graph[nx][ny] = 1

    result = max(result, path)


for i in range(N):
    flag = False
    for j in range(M):
        if graph[i][j] == 0:
            result = -1
            flag = True
            break

    if flag:
        break

print(result)





