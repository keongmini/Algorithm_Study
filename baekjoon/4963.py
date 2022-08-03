# dfs 풀이
# pypy 통과 / python3 runtime error
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x - 1, y + 1)
        dfs(x, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y - 1)
        dfs(x, y - 1)
        dfs(x - 1, y - 1)
        return True
    return False

while True:
    m,n = map(int, input().split())
    if m == 0 & n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)


# bfs 풀이
# pypy, python3 통과
from collections import  deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))


while True:
    m, n = map(int, input().split())
    if m == 0 & n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)
