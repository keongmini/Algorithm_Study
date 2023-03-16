from collections import deque

N, L, R = map(int,input().split())

graph = []
for _ in range(N):
    new = list(map(int, input().split()))
    graph.append(new)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a,b):
    q = deque([(a, b)])
    groupList = [(a, b)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny] != 0:
                continue

            now = abs(graph[nx][ny] - graph[x][y])
            if now >= L and now <= R:
                visited[nx][ny] = 1
                q.append((nx, ny))
                groupList.append((nx, ny))

    return groupList


result = 0
while True:
    visited = [[0] * (N) for _ in range(N)]
    check = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                group = bfs(i, j)

                if len(group) > 1:
                    check = 1

                    sumNum = 0
                    for x, y in group:
                        sumNum += group[x][y]

                    num = sumNum // len(group)

                    for x, y in group:
                        graph[x][y] = num

    if check == 0:
        break

    result += 1

print(result)