# 참고 https://jshong1125.tistory.com/29

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque([N])

visited = [-1 for _ in range(100001)]
visited[N] = 0

while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        break

    if 0 <= now - 1 < 100001 and visited[now - 1] == -1:            # - 부터 처리해주어야 함 (작은 값부터 해야 최소값이 나오는 걸로 예상..)
        q.append(now - 1)
        visited[now - 1] = visited[now] + 1

    if 0 <= now * 2 < 100001 and visited[now * 2] == -1:
        q.appendleft(now * 2)
        visited[now * 2] = visited[now]

    if 0 <= now + 1 < 100001 and visited[now + 1] == -1:
        q.append(now + 1)
        visited[now + 1] = visited[now] + 1

# 주의할점
# 1. -1 로 초기화해서 방문처리 해주기
# 2. + 전에 - 먼저 처리해주기
# 3. *2 하는 경우 appendleft해서 우선적으로 처리되도록(우선순위가 높음)
# 4. 위 과정을 거치기 때문에 최소값 비교 필요 x