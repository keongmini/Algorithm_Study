from collections import defaultdict

def solution(N, stages):
    nums = defaultdict(int)

    for stage in stages:
        nums[stage] += 1

    rate = []
    now = len(stages)
    for i in range(1, N + 1):
        if now == 0:
            rate.append((0, i))
        else:
            rate.append((nums[i] / now, i))

        now -= nums[i]

    rate.sort(key=lambda x: -x[0])

    result = []
    for r in rate:
        result.append(r[1])

    return result