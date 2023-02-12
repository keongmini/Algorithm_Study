import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
nums = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    nums[x].append(y)

result = []
visited = [False for _ in range(N + 1)]
visited[0] = True

q = deque([(X, 0)])
visited[X] = True

while q:
    now, length = q.popleft()

    if length == K:
        result.append(now)
        continue

    for num in nums[now]:
        if not visited[num]:
            visited[num] = True
            q.append((num, length + 1))

if not result:
    print(-1)
else:
    result.sort()
    for r in result:
        print(r)
