# # 메모리 초과 - 반례: N, S, M = 50, 500, 1000 / P = [1] * 50
# from collections import deque
#
# N, S, M = map(int, input().split())
#
# P = list(map(int, input().split()))
#
# now = deque([S])
#
# flag = True
# for p in P:
#     if not now:
#         flag = False
#         break
#
#     t = len(now)
#
#     for _ in range(t):
#         n = now.popleft()
#
#         if n - p >= 0:
#             now.append(n - p)
#
#         if n + p <= M:
#             now.append(n + p)
#
# if not flag:
#     print(-1)
# else:
#     print(max(now))
#

# dp - 통과
N, S, M = map(int, input().split())
P = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = 1

for i in range(N):
    for j in range(M + 1):
        if dp[i][j] == 1:
            if j + P[i] <= M:
                dp[i + 1][j + P[i]] = 1     # 현재 결과를 그 다음 배열에 저장

            if j - P[i] >= 0:
                dp[i + 1][j - P[i]] = 1

result = -1
for i in range(M, -1, -1):
    if dp[N][i] == 1:
        result = i
        break

print(result)