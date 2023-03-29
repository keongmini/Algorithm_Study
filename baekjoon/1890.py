# # DFS - 메모리 초과
# # 방문처리해줘도 안됨
# from collections import deque
#
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# graph = []
# for _ in range(N):
#     now = list(map(int, input().split()))
#     graph.append(now)
#
# q = deque([(0, 0)])
#
# move = [(1, 0), (0, 1)]
#
# result = 0
# while q:
#     x, y = q.popleft()
#     now = graph[x][y]
#
#     for a, b in move:
#         nx = x + now * a
#         ny = y + now * b
#
#         if nx < 0 or nx >= N or ny < 0 or ny >= N:
#             continue
#
#         if graph[nx][ny] == 0:
#             result += 1
#             continue
#
#         q.append((nx, ny))
#
# print(result)

# dp
# 탐색 수 누적
import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    now = list(map(int, input().split()))
    graph.append(now)

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):

        if i == N - 1 and j == N - 1:
            break

        left = j + graph[i][j]
        if left < N:
            dp[i][left] += dp[i][j]

        down = i + graph[i][j]
        if down < N:
            dp[down][j] += dp[i][j]

print(dp[N - 1][N - 1])