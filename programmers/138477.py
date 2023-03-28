import heapq


def solution(k, score):
    result = []

    now = []
    for s in score:
        if len(now) < k:
            heapq.heappush(now, s)
            result.append(min(now))
        else:
            if min(now) < s:
                heapq.heappop(now)
                heapq.heappush(now, s)
            result.append(min(now))

    return result