T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    start = 0
    for i in range(n):
        new = array[start:start + m]
        dp.append(new)
        start += m

    for j in range(1, m):
        for i in range(n):

            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)