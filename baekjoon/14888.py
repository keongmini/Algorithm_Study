N = int(input())

nums = list(map(int, input().split()))

operator = list(map(int, input().split()))      # +, -, *, /

max_result = -1e9
min_result = 1e9


def dfs(now, op, idx):
    global max_result, min_result

    if op == 0:
        now += nums[idx]
    elif op == 1:
        now -= nums[idx]
    elif op == 2:
        now *= nums[idx]
    elif op == 3:
        if now < 0:
            now = -now
            now //= nums[idx]
            now = -now
        else:
            now //= nums[idx]

    if idx == N - 1:
        max_result = max(max_result, now)
        min_result = min(min_result, now)
        return

    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            dfs(now, i, idx + 1)
            operator[i] += 1


for i in range(4):
    if operator[i]:
        operator[i] -= 1
        dfs(nums[0], i, 1)
        operator[i] += 1

print(int(max_result))
print(int(min_result))
# 소수점 출력 방지를 위해 int 처리 필요


# 틀렸습니다.
# N = int(input())
# A = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
#
# maxNum = -1e9
# minNum = 1e9
#
# def dfs(cnt, num):
#     global add, sub, mul, div, maxNum, minNum
#
#     if cnt == N:
#         maxNum = max(maxNum, num)
#         minNum = min(minNum, num)
#     else:
#         if add > 0:
#             add -= 1
#             dfs(cnt + 1, num + A[cnt])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(cnt + 1, num - A[cnt])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(cnt + 1, num * A[cnt])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(cnt + 1, int(num / A[cnt]))
#             div += 1
#
# dfs(1, A[0])
#
# print(maxNum)
# print(minNum)