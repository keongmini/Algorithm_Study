import sys

input = sys.stdin.readline

N, C = list(map(int, input().split()))

loc = []
for _ in range(N):
    loc.append(int(input()))
loc.sort()

start = 1
end = loc[-1] - loc[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    now = loc[0]
    cnt = 1

    for i in range(1, N):
        if loc[i] >= now + mid:
            now = loc[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)