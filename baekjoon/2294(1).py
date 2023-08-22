import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = set()

for _ in range(n):
    tmp = int(input())

    if tmp <= k:
        coin.add(tmp)

coin = list(coin)
coin.sort()

result = [1e9 if num not in coin else 1 for num in range(k + 1)]

for i in range(1, k + 1):

    for c in coin:
        now = i - c

        if now <= 0:
            break

        result[i] = min(result[i], result[now] + 1)

if result[k] == 1e9:
    print(-1)
else:
    print(result[k])

