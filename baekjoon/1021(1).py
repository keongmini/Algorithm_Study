import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
location = list(map(int, input().split()))

nums = deque([i for i in range(1, N + 1)])

result = 0

for i in location:
    idx = nums.index(i)

    if idx < N - idx:
        for _ in range(idx):
            nums.append(nums.popleft())
            result += 1

    else:
        for _ in range(N - idx):
            nums.appendleft(nums.pop())
            result += 1

    nums.popleft()
    N -= 1

print(result)