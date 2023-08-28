import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[s for s in input()] for _ in range(R)]
visited = [[False for i in range(C)] for _ in range(R)]

move = [(-1, 1), (0, 1), (1, 1)]


def dfs(x, y):
    if y == C - 1:
        return True

    for a, b in move:
        nx = x + a
        ny = y + b

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        if visited[nx][ny] or graph[nx][ny] == 'x':
            continue

        visited[nx][ny] = True

        if dfs(nx, ny):
            return True

    return False


result = 0
for i in range(R):
    if dfs(i, 0):
        result += 1

print(result)