import heapq


def solution(jobs):
    total, prev = 0, 0
    start = -1
    q = []

    n = len(jobs)

    while n > 0:
        for order, spend in jobs:
            if start < order and order <= prev:
                heapq.heappush(q, (spend, order))

        if q:
            spend, order = heapq.heappop(q)
            start = prev
            prev += spend
            total += prev - order
            n -= 1
        else:
            prev += 1

    return int(total / len(jobs))

s = solution([[0, 3], [1, 9], [2, 6]])