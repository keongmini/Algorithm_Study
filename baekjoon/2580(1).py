import sys

input = sys.stdin.readline

location = []

graph = []
for i in range(9):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

    for j in range(9):
        if tmp[j] == 0:
            location.append((i, j))


def row(i, n):
    for j in range(9):
        if graph[i][j] == n:
            return False

    return True


def column(j, n):
    for i in range(9):
        if graph[i][j] == n:
            return False

    return True


def rectangular(i, j, n):
    ni = (i // 3) * 3
    nj = (j // 3) * 3

    for a in range(3):
        for b in range(3):
            if n == graph[ni + a][nj + b]:
                return False

    return True


def check(cnt):
    if cnt == len(location):
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=" ")
            print()

        exit()

    for num in range(1, 10):
        nx = location[cnt][0]
        ny = location[cnt][1]

        if row(nx, num) and column(ny, num) and rectangular(nx, ny, num):
            graph[nx][ny] = num
            check(cnt + 1)
            graph[nx][ny] = 0


check(0)



