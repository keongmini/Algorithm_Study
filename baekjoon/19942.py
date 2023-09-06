import sys

input = sys.stdin.readline

N = int(input())

mp, mf, ms, mv = map(int, input().split())

nutrient = [list(map(int, input().split())) for _ in range(N)]

result = 1e9
result_nums = []


def check(idx, p, f, s, v, c, now):
    global result, result_nums

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if result > c:                                  # 작은지만 비교하기 때문에 정렬 필요 x
            result = c
            result_nums = now.copy()                    # copy()로 얕은 복사
        return

    for j in range(idx + 1, N):
        tp, tf, ts, tv, tc = nutrient[j]

        now.append(j + 1)
        check(j, p + tp, f + tf, s + ts, v + tv, c + tc, now)
        now.pop()


for i in range(N):
    p, f, s, v, c = nutrient[i]
    check(i, p, f, s, v, c, [i + 1])

if result == 1e9:
    print(-1)
else:
    print(result)
    for num in result_nums:
        print(num, end=" ")