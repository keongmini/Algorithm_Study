# dp - 통과
import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split()))for _ in range(N)]

for i in range(1, N):
    graph[i][0] = graph[i][0] + min(graph[i - 1][1], graph[i - 1][2])
    graph[i][1] = graph[i][1] + min(graph[i - 1][0], graph[i - 1][2])
    graph[i][2] = graph[i][2] + min(graph[i - 1][0], graph[i - 1][1])

print(min(graph[N - 1]))


# dfs - 시간초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N = int(input())
#
# colors = [{}]
#
# for _ in range(N):
#     now = {}
#
#     tmp = list(map(int, input().split()))
#
#     now['R'] = tmp[0]
#     now['G'] = tmp[1]
#     now['B'] = tmp[2]
#
#     colors.append(now)
#
# result = 1e9
#
# for c in colors[1]:
#     q = deque()
#     q.append((c, colors[1][c], 1))          # 현재 색깔, 현재까지 값, 현재 집 번호
#
#     while q:
#         now_color, cnt, now = q.popleft()
#
#         if now == N:
#             result = min(result, cnt)
#             continue
#
#         for nc in colors[now + 1]:
#             if nc == now_color:
#                 continue
#
#             q.append((nc, cnt + colors[now + 1][nc], now + 1))
#
# print(result)