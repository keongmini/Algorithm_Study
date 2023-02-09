def solution(N, stages):
    rate = [[0, i + 1] for i in range(N)]

    stages.sort()

    total = len(stages)

    for i in range(1, N + 1):
        if i > N or total == 0:
            break

        cnt = stages.count(i)
        rate[i - 1][0] = cnt / total
        total -= cnt

    rate.sort(key=lambda x: (-x[0], x[1]))

    result = []
    for r in rate:
        result.append(r[1])

    return result
