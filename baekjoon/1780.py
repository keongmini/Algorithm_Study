import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

result = {-1: 0, 0: 0, 1: 0}


def check(r, c, n):
    now = graph[r][c]                           # 종이의 첫번째 값

    for i in range(r, r + n):
        for j in range(c, c + n):
            if graph[i][j] != now:              # 값이 다름 -> 종이 쪼개기
                next_n = n // 3

                # 종이를 열 기준으로 3등분했을 때 첫째줄
                check(r, c, next_n)
                check(r, c + next_n, next_n)
                check(r, c + (next_n * 2), next_n)

                # 종이를 열 기준으로 3등분했을 때 둘째줄
                check(r + next_n, c, next_n)
                check(r + next_n, c + next_n, next_n)
                check(r + next_n, c + (next_n * 2), next_n)

                # 종이를 열 기준으로 3등분했을 때 셋째줄
                check(r + (next_n * 2), c, next_n)
                check(r + (next_n * 2), c + next_n, next_n)
                check(r + (next_n * 2), c + (next_n * 2), next_n)
                return                                  # 종이 갯수 세지 않도록 return 처리

    result[now] += 1


check(0, 0, N)

for k in result:
    print(result[k])