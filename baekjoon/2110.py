import sys

input = sys.stdin.readline

N, C = list(map(int, input().split()))

loc = []
for _ in range(N):
    loc.append(int(input()))
loc.sort()

start = 1     # 가장 짧은 거리
end = loc[-1] - loc[0]      # 가장 긴 거리

result = 0
while start <= end:
    mid = (start + end) // 2
    now = loc[0]            # 첫번째 집에 공유기 설치 했다고 가정
    cnt = 1                 # 설치한 공유기 갯수 (첫번째 집에 설치되어있으니 1)

    for i in range(1, N):           # 끝까지 돌면서 C개 설치할 수 있는지 확인
        if loc[i] >= now + mid:
            now = loc[i]            # 그 다음으로 설치한 집
            cnt += 1

    if cnt >= C:
        start = mid + 1             # 거리를 더 넓혀보기
        result = mid
    else:
        end = mid - 1               # C개까지 설치하지 못했으니까 거리 좁히기

print(result)