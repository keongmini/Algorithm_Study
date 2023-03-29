# 시간초과

# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# T = [0 for _ in range(N + 1)]
# P = [0 for _ in range(N + 1)]
# for i in range(N):
#     t, p = map(int, input().split())
#     T[i + 1] = t
#     P[i + 1] = p
#
# dp = [p for p in P]
#
# for i in range(1, N + 1):
#     if i + T[i] > N + 1:
#         dp[i] = 0
#         continue
#
#     for j in range(i + T[i], N + 1):
#         if j + T[j] > N + 1:
#             continue
#         dp[j] = max(dp[j], dp[i] + P[j])
#
# print(max(dp))


import sys
input = sys.stdin.readline

N = int(input())

T = [0 for _ in range(N + 1)]
P = [0 for _ in range(N + 1)]
for i in range(N):
    t, p = map(int, input().split())
    T[i + 1] = t
    P[i + 1] = p

dp = [0 for _ in range(N + 2)]

k = 0
for i in range(1, N + 1):
    k = max(k, dp[i])

    if i + T[i] > N + 1:
        continue
    dp[i + T[i]] = max(k + P[i], dp[i + T[i]])

print(max(dp))

