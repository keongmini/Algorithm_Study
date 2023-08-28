N = int(input())

if N == 3 or N == 5:
    print(1)
    exit()

if N == 4:
    print(-1)
    exit()

dp = [1e9 for _ in range(N + 1)]
dp[3] = 1
dp[5] = 1

for i in range(6, N + 1):
    dp[i] = min(dp[i], dp[i - 3] + 1)

    dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[N] == 1e9:
    print(-1)
else:
    print(dp[N])
