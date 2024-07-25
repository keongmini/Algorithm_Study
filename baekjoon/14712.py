N, M = map(int, input().split())

graph = [[0 for _ in range(M + 1)] for i in range(N + 1)]
result = 0


def dfs(cnt):
    global result

    if cnt == N * M:
        result += 1
        return

    x = cnt // M + 1
    y = cnt % M + 1

    if graph[x - 1][y] == 0 or graph[x - 1][y - 1] == 0 or graph[x][y - 1] == 0:
        graph[x][y] = 1
        dfs(cnt + 1)
        graph[x][y] = 0

    dfs(cnt + 1)


dfs(0)
print(result)