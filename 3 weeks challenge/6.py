import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    prev = 0
    while q:
        time, index = q[0]
        now = (time - prev) * len(q)

        if now < k:
            k -= now
            prev = heapq.heappop(q)[0]
        else:
            q.sort(key=lambda x: x[1])
            final_index = k % len(q)
            return q[final_index][1]

