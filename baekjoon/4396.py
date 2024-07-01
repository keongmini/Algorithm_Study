import sys

input = sys.stdin.readline
move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def check(x, y):
    result = 0

    for a, b in move:
        nx = x + a
        ny = y + b

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == "*":
            result += 1

    return result


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
nums = [list(input().rstrip()) for _ in range(n)]
result = [["." for i in range(n)] for j in range(n)]

flag = False

for i in range(n):
    for j in range(n):
        if nums[i][j] == "x":
            if graph[i][j] == "*":
                flag = True
            result[i][j] = check(i, j)

if flag:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "*":
                result[i][j] = "*"

for r in result:
    print(*r, sep="")

