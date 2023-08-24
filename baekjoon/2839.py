N = int(input())

# 이 코드에서 따로 처리 필요한 부분 - 안해주면 런타임에러 발생
if N == 3:
    print(1)
    exit()

if N < 5:
    print(-1)
    exit()

result = [1e9 for _ in range(N + 1)]
result[3] = 1
result[5] = 1

for num in range(N + 1):
    if num - 3 > 0:
        result[num] = min(result[num], result[num - 3] + 1)

    if num - 5 > 0:
        result[num] = min(result[num], result[num - 5] + 1)

if result[N] == 1e9:
    print(-1)
else:
    print(result[N])