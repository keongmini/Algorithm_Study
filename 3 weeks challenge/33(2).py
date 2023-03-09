N = int(input())

T = []
P = []
for _ in range(N):
    n, m = map(int, input().split())
    T.append(n)
    P.append(m)

dp = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i + T[i], N + 1):
        dp[j] = max(dp[j], dp[i] + P[i])

print(max(dp))