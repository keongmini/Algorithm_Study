import heapq
N = int(input())

q = []
for _ in range(N):
    heapq.heappush(q, int(input()))

if N == 1:
    print(0)
else:
    result = 0
    while len(q) > 1:
        now1 = heapq.heappop(q)
        now2 = heapq.heappop(q)

        now = now1 + now2
        result += now
        heapq.heappush(q, now)

    print(result)



