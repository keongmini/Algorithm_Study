import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[s for s in input()] for _ in range(R)]

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = set()
q.add((0, 0, 1, graph[0][0]))

result = 0

while q:
    x, y, cnt, passed = q.pop()

    for a, b in move:
        nx = x + a
        ny = y + b

        if nx < 0 or nx >= R or ny < 0 or ny >= C or graph[nx][ny] in passed:
            continue

        q.add((nx, ny, cnt + 1, passed + graph[nx][ny]))

    result = max(result, cnt)

print(result)