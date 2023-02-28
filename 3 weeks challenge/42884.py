import heapq


def solution(routes):
    q = []

    for x, y in routes:
        heapq.heappush(q, (x, y))

    start, end = heapq.heappop(q)

    result = 0
    while q:
        x, y = heapq.heappop(q)

        if start <= x <= end:
            start = max(start, x)
            end = min(end, y)
        else:
            result += 1
            start = x
            end = y

    result += 1
    return result