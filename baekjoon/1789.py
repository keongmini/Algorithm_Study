S = int(input())

tot = 0
cnt = 0

while True:
    cnt += 1
    tot += cnt

    if tot > S:         # 갯수만 구하면 되기 때문에 커졌을 경우 stop - 숫자를 분배해주면 됨
        break

print(cnt - 1)