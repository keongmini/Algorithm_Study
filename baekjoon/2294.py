import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = set()            # 중복 제거

for _ in range(n):
    tmp = int(input())
    if tmp <= k:
        coin.add(tmp)

coin = list(coin)
coin.sort()             # 작은 수 부터 확인

dp = [1e9 if i not in coin else 1 for i in range(k + 1)]

for i in range(1, k + 1):
    for c in coin:
        now = i - c

        if now <= 0:            # 1부터 시작이니까
            break

        dp[i] = min(dp[i], dp[now] + 1)         # 현재 값과 이전 값 + 1 비교

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])


# for c in coin:
#     dp[c] = 1
#
#     for n in range(c + c, k + 1, c):
#         dp[n] = min(dp[n], dp[n - c] + 1)

