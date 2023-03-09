def solution(money):
    # 마지막 집 x - 첫번째부터 시작 가능
    dp1 = [0 for _ in money]
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 마지막 집 o - 첫번째 집 x
    dp2 = [0 for _ in money]
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1), max(dp2))