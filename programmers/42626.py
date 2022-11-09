import heapq
def solution(scoville, K):
    if len(scoville) == 1 and scoville[0] >= K:
        return 0

    q = []
    for s in scoville:
        heapq.heappush(q, s)

    result = 0
    while q:
        if len(q) == 1 and q[0] < K:        # 요소가 1개 남았을 때 따로 처리해주어야 함
            return -1

        if q[0] >= K:
            return result

        n = heapq.heappop(q)
        m = heapq.heappop(q)

        now = n + (m * 2)
        heapq.heappush(q, now)

        result += 1

    return -1

