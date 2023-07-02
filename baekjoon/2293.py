n, k = map(int, input().split())
data = []

for _ in range(n):
    now = int(input())
    data.append(now)

dp = [0 for i in range(k + 1)]      # 1부터 주어진 가치 값까지 모든 값에 대한 경우의 수 누적
dp[0] = 1                           # 동전 한개를 사용하는 경우 처리하기 위해(어처피 0원은 없음) ex) dp[2] = dp[2] += dp[0] = 0 + 1 = 1

for i in data:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
            # 현재 동전이 2인 경우,
            # dp[5] = 지금까지 dp[5]를 구하기 위한 경우의 수 + dp[3]을 구할 수 있는 경우(이 모든 경우에 2를 더하면 5가 되기 때문에)

print(dp[k])