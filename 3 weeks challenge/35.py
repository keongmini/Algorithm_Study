n = int(input())

dp = [0 for _ in range(n + 1)]
dp[1] = 1

two = three = five = 1      # 두번째, 세번째, 네번째 값 인덱스 1에서 시작
next2, next3, next5 = 2, 3, 5

for i in range(2, n + 1):
    dp[i] = min(next2, next3, next5)        # 가장 작은 값부터 처리해주기 위해

    if dp[i] == next2:
        two += 1            # 인덱스 + 1
        next2 = dp[two] * 2     # 현재 값에서 2를 곱한 값
    if dp[i] == next3:
        three += 1
        next3 = dp[three] * 3
    if dp[i] == next5:
        five += 1
        next5 = dp[five] * 5

print(dp[n])