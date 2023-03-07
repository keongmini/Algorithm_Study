from itertools import combinations

N, M = map(int, input().split())

homes = []      # 집의 좌표
chickens = []       # 치킨집의 좌표

for i in range(N):
    new = list(map(int, input().split()))
    for j in range(N):
        if new[j] == 1:
            homes.append((i, j))
        elif new[j] == 2:
            chickens.append((i, j))

result = 1e9

for chicken in combinations(chickens, M):       # 모든 조합 모두 확인
    tmp = 0

    for x, y in homes:
        length = 1e9

        for i in range(M):
            now = chicken[i]
            length = min(length, abs(x - now[0]) + abs(y - now[1]))     # 현재 집에서 가장 가까운 치킨집 구하기 (조합 내에 있는 치킨 집 중)

        tmp += length

    result = min(result, tmp)

print(result)