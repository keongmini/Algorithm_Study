import heapq
def solution(jobs):
    total, now, i = 0, 0, 0
    start = -1
    q = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, [job[1], job[0]])

        if len(q) > 0:
            cur = heapq.heappop(q)
            start = now
            now += cur[0]
            total += now - cur[1]
            i += 1
        else:
            now += 1

    return int(total / len(jobs))
