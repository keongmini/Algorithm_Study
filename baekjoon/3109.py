# 참고: https://recordofwonseok.tistory.com/370

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[s for s in input()] for _ in range(R)]

visited = [[False for i in range(C)] for _ in range(R)]


def dfs(x, y):
    if y == C - 1:                      # 빵집 도착
        return True

    for a in [-1, 0, 1]:
        nx = x + a
        ny = y + 1                      # 열은 한칸씩 계속 이동

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


