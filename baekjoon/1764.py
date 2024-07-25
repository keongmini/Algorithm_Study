from collections import defaultdict

N, M = map(int, input().split())
check = defaultdict(int)

for _ in range(N + M):
    new = input()
    check[new] += 1

result = []

for k in check:
    if check[k] >= 2:
        result.append(k)

result.sort()

print(len(result))
for r in result:
    print(r)