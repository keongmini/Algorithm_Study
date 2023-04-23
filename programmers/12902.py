def solution(n):
    if n % 2 == 1:
        return 0

    dp = [0 for _ in range(n + 1)]
    dp[2] = 3
    dp[4] = 11

    for i in range(6, n + 1, 2):
        dp[i] = (dp[i - 2] * 4 - dp[i - 4]) % 1000000007

    return dp[n]


# 참고 https://velog.io/@yujeongkwon/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-PYTHON-3-x-n-%ED%83%80%EC%9D%BC%EB%A7%81 (DP)
# 점화식: F(n) = F(n - 2) * 4 - F(n - 4)