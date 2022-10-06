N = int(input())

graph = []
for _ in range(N):
    graph.append([int(n) for n in input()])

visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N or graph[x][y] != 1 or visited[x][y]:
        return

    visited[x][y] = True
    cnt += 1

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()               # 정렬 주의! 
for n in result:
    print(n)
