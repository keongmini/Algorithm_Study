import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = set()

for _ in range(n):
    tmp = int(input())
    if tmp <= k:
        coin.add(tmp)

coin = list(coin)
coin.sort()

dp = [1e9 if i not in coin else 1 for i in range(k + 1)]

for i in range(1, k + 1):
    for c in coin:
        now = i - c

        if now <= 0:
            break

        dp[i] = min(dp[i], dp[now] + 1)

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])


# for c in coin:
#     dp[c] = 1
#
#     for n in range(c + c, k + 1, c):
#         dp[n] = min(dp[n], dp[n - c] + 1)

