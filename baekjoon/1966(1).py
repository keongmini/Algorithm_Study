import sys
import heapq
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    importance = list(map(int, input().split()))
    q = []

    nums = deque()
    for i in range(N):
        nums.append((i, importance[i]))
        heapq.heappush(q, -importance[i])

    cnt = 0
    while True:

        if -q[0] == nums[0][1] and nums[0][0] == M:
            print(cnt + 1)
            break

        if -q[0] > nums[0][1]:
            nums.append(nums.popleft())

        elif -q[0] == nums[0][1]:
            cnt += 1
            heapq.heappop(q)
            nums.popleft()


