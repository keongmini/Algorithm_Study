N, S = map(int, input().split())

nums = list(map(int, input().split()))

result = 0


def dfs(i, now):
    global result

    if i == N :
        return

    now += nums[i]

    if now == S:
        result += 1

    dfs(i + 1, now)
    dfs(i + 1, now - nums[i])


dfs(0, 0)
print(result)