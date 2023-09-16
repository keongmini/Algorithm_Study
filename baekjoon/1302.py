from collections import defaultdict

N = int(input())

d = defaultdict(int)

for _ in range(N):
    now = input()
    d[now] += 1

result = 0
cnt = 0

for k in d:
    if d[k] > cnt:
        cnt = d[k]
        result = k
    if d[k] == cnt:
        result = min(result, k)

print(result)