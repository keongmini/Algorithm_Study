import sys

input = sys.stdin.readline

n = int(input())
volume = [int(input()) for _ in range(n)]

if n < 3:                   # 예외 사항 처리 필수
    print(sum(volume))
    exit()

dp = [0 for _ in range(n)]
dp[0] = volume[0]
dp[1] = volume[0] + volume[1]
dp[2] = max(volume[0] + volume[2], volume[1] + volume[2], dp[1])

for i in range(3, n):
    dp[i] = max(volume[i] + dp[i - 2], volume[i] + volume[i - 1] + dp[i - 3], dp[i - 1])

print(max(dp))