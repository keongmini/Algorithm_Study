# 모든 숫자는 1만으로 구할 수 있음 - 한개 누적
dp = [1] * 10001

for i in range(2, 10001):       # [현재-2] 인 경우에 2를 더해준 경우
    dp[i] += dp[i - 2]

for i in range(3, 10001):       # [현재-3] 인 경우에 3를 더해준 경우
    dp[i] += dp[i - 3]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])