import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(nums))
    exit()

dp = [0 for _ in range(n)]
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]
dp[2] = max(dp[1], nums[0] + nums[2], nums[1] + nums[2])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i], dp[i - 3] + nums[i - 1] + nums[i])

print(max(dp))