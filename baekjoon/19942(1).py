import sys

input = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(N)]

result = 1e9
result_nums = []


def check(idx, p, f, s, v, c, nums):
    global result, result_nums

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if result > c:
            result = c
            result_nums = nums.copy()
        return True

    for j in range(idx + 1, N):
        np, nf, ns, nv, nc = nutrient[j]
        nums.append(j + 1)
        check(j, p + np, f + nf, s + ns, v + nv, c + nc, nums)
        nums.pop()


for i in range(N):
    p, f, s, v, c = nutrient[i]
    check(i, p, f, s, v, c, [i + 1])

if result == 1e9:
    print(-1)
else:
    print(result)
    for n in result_nums:
        print(n, end=" ")