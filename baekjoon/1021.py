import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

nums = deque([i for i in range(1, N + 1)])

check_nums = list(map(int, input().split()))

result = 0

for num in check_nums:
    idx = nums.index(num)

    if idx <= N - idx:                      # 왼쪽으로 빼는 게 빠른 경우
        for _ in range(idx):
            nums.append(nums.popleft())
            result += 1

        nums.popleft()

    else:                                   # 오른쪽으로 빼는 게 빠른 경우
        for _ in range(N - idx):
            nums.appendleft(nums.pop())
            result += 1

        nums.popleft()

    N -= 1

print(result)



