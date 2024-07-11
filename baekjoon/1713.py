import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))

q = []
cnt = defaultdict(int)

for num in nums:
    if len(q) == N and num not in cnt:
        minNum = min(q, key=lambda x: cnt[x])
        q.remove(minNum)
        del cnt[minNum]

    if num in cnt:
        cnt[num] += 1
    elif len(q) < N:
        q.append(num)
        cnt[num] += 1

q.sort()
for n in q:
    print(n, end=" ")



