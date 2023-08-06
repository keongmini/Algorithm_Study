# bfs, set - 통과
import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[s for s in input()] for _ in range(R)]

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    result = 1

    s = set()
    s.add((x, y, 1, graph[x][y]))

    while s:
        i, j, cnt, passed = s.pop()         # passed = 문자열 - 문자열에 계속 누적해서 값 저장

        for a, b in move:
            nx = i + a
            ny = j + b

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if graph[nx][ny] in passed:
                continue

            s.add((nx, ny, cnt + 1, passed + graph[nx][ny]))

        result = max(result, cnt)

    return result


print(bfs(0, 0))


# dfs, 딕셔너리 - 시간 초과
# import sys
#
# input = sys.stdin.readline
#
# R, C = map(int, input().split())
#
# graph = [[s for s in input()] for _ in range(R)]
#
# visited = {}
#
# result = 1
#
# move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#
# def dfs(x, y, cnt):
#     global result
#
#     result = max(result, cnt)
#
#     visited[graph[x][y]] = True
#
#     for a, b in move:
#         nx = x + a
#         ny = y + b
#
#         if nx < 0 or nx >= R or ny < 0 or ny >= C or graph[nx][ny] in visited:
#             continue
#
#         dfs(nx, ny, cnt + 1)
#
#     del visited[graph[x][y]]
#
#
# dfs(0, 0, 1)
#
# print(result)