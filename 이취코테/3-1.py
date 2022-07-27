n = 1260
coins = [500, 100, 50, 10]
cnt = 0

for coin in coins:
    cnt += n // coin
    n %= coin

print(cnt)