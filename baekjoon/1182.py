# 재귀 풀이 - 통과
N, S = map(int, input().split())
nums = list(map(int, input().split()))

result = 0


def dfs(i, cnt):
    global result

    if i == N:
        return

    cnt += nums[i]

    if cnt == S:
        result += 1

    dfs(i + 1, cnt)         # 현재 값에 누적
    dfs(i + 1, cnt - nums[i])           # 현재 값 제외하고


dfs(0, 0)
print(result)


# itertools 라이브러리 사용 - 통과
import itertools

N, S = map(int, input().split())
nums = list(map(int, input().split()))

result = 0

for i in range(1, N + 1):
    permutation = itertools.combinations(nums, i)

    for p in permutation:
        if sum(p) == S:
            result += 1

print(result)