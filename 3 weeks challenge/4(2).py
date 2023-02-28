N = int(input())
coins = list(map(int, input().split()))
coins.sort()

result = 1
for coin in coins:
    if coin > result:
        break
    result += coin

print(result)
