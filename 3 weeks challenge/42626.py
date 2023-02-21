import heapq


def solution(scoville, K):
    q = []

    for s in scoville:
        heapq.heappush(q, s)

    result = 0
    while q:

        if len(q) == 1:
            if q[0] < K:
                return -1
            else:
                return result

        first = heapq.heappop(q)
        second = heapq.heappop(q)

        if first >= K:
            return result

        new = first + (second * 2)
        heapq.heappush(q, new)

        result += 1

    return -1
