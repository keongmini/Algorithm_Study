import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i, time in enumerate(food_times):
        heapq.heappush(q, (time, i + 1))

    prev = 0
    while q:
        time, i = q[0]
        now = (time - prev) * len(q)

        if now < k:
            k -= now
            prev = heapq.heappop(q)[0]
        else:
            q.sort(key=lambda x: x[1])
            end = k % len(q)
            return q[end][1]
