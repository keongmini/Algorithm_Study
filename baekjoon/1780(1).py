import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

result = {-1: 0, 0: 0, 1: 0}


def check(x, y, n):
    now = graph[x][y]

    for r in range(x, x + n):
        for c in range(y, y + n):
            if graph[r][c] != now:
                size = n // 3

                check(x, y, size)                   # x, y 주의
                check(x, y + size, size)
                check(x, y + (size * 2), size)

                check(x + size, y, size)
                check(x + size, y + size, size)
                check(x + size, y + (size * 2), size)

                check(x + (size * 2), y, size)
                check(x + (size * 2), y + size, size)
                check(x + (size * 2), y + (size * 2), size)
                return

    result[now] += 1


check(0, 0, N)

for k in result:
    print(result[k])

