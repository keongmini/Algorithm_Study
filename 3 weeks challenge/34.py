N = int(input())
soldier = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if soldier[j] < soldier[i]:
            dp[j] = max(dp[j], dp[i] + 1)

print(N - max(dp))