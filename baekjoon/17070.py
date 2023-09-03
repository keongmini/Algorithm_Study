# dp - 통과
# 참고 https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python

# 가로, 세로, 대각선으로 이동 가능한 경우의 수를 경우별로 저장해서 다 더하는 방식
def check():
    dp[0][0][1] = 1             # 가로 파이프의 (0, 1) 좌표에서 시작하니까 이미 방문

    # 그래프의 첫번째 줄은 무조건 방문 가능 - 가로로 시작하기 때문에 가로로 계속 이동하면 됨(벽이 아닌 이상)
    for i in range(2, N):
        if graph[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    # 1부터 시작하는 이유: 그래프의 1열은 무조건 방문 불가 - 가로로 시작하기 떄문에 세로로 바꿔서 첫열에 방문 불가
    for r in range(1, N):
        for c in range(1, N):

            # 대각선으로 이동하는 경우 - 가로, 세로, 대각선이 모두 벽이 아니어야 함
            if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:
                # 가로, 세로, 대각선 모두 대각선으로 이동 가능 - 각각의 경우의 수를 모두 더하기
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            # 가로, 세로인 경우 - 하나의 칸(이동하려는 칸)만 벽이 아니면 됨
            if graph[r][c] == 0:
                # 가로, 대각선만 가로로 이동 가능 - 가로, 대각선의 경우의 수 더하기
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                # 세로, 대각선만 세로로 이동 가능 - 세로, 대각선의 경우의 수 더하기
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    # 가로, 세로, 대각선으로 이동해서 마지막 칸에 도착한 경우의 수 모두 더하기
    result = 0
    for i in range(3):
        result += dp[i][N - 1][N - 1]

    return result


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
# 3차원인 이유: 가로(0), 세로(2), 대각선(1) 가능한 경우의 수 각각 저장
print(check())


# # 그래프 - 시간초과
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
#
# graph = [list(map(int, input().split())) for _ in range(N)]
#
# ways = {
#     'r': [(0, 1, 'r'), (1, 1, 'd')],
#     'c': [(1, 0, 'c'), (1, 1, 'd')],
#     'd': [(1, 0, 'c'), (1, 1, 'd'), (0, 1, 'r')]
# }
#
# x, y = 0, 1
#
# result = set()
#
#
# def check(a, b, path):
#
#     if a == N - 1 and b == N - 1:
#         result.add(tuple(path))
#         return
#
#     for di, dj, dw in ways[path[-1]]:
#         na = a + di
#         nb = b + dj
#
#         if na >= N or nb >= N or graph[na][nb] == 1:
#             continue
#
#         if dw == 'd' and (graph[na - 1][nb] == 1 or graph[na][nb - 1]):
#             continue
#
#         path.append(dw)
#         check(na, nb, path)
#         path.pop()
#
#
# check(x, y, ['r'])
#
# print(len(result))