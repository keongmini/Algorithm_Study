# 시간초과
from collections import defaultdict, deque

def solution(n, edge):
    path = defaultdict(list)

    for x, y in edge:
        path[x].append(y)
        path[y].append(x)

    result = [5001 for _ in range(n + 1)]

    q = deque([(1, 0)])

    while q:
        now, cnt = q.popleft()
        result[now] = min(result[now], cnt)

        for p in path[now]:
            q.append((p, cnt + 1))
            path[p].remove(now)

    maxNum = max(result)

    return result.count(maxNum)

# 통과
from collections import defaultdict
import heapq

def solution(n, edge):
    path = defaultdict(list)

    for x, y in edge:
        path[x].append(y)
        path[y].append(x)

    result = [5001 for _ in range(n + 1)]

    q = []

    heapq.heappush(q, (0, 1))
    result[0] = 0
    result[1] = 1

    while q:
        cnt, now = heapq.heappop(q)

        if result[now] < cnt:
            continue

        for p in path[now]:
            if cnt + 1 < result[p]:
                result[p] = cnt + 1
                heapq.heappush(q, (cnt + 1, p))

    maxNum = max(result)

    return result.count(maxNum)

s = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(s)