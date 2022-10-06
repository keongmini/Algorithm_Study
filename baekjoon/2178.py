import collections

N, M = map(int, input().split())
N -= 1
M -= 1

graph = []
for _ in range(N + 1):
    graph.append([int(i) for i in input()])

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = int(1e9)
q = collections.deque([(0, 0)])
while q:
    nowx, nowy = q.popleft()

    for x, y in d:
        if nowx + x < 0 or nowx + x > N or nowy + y < 0 or nowy + y > M or graph[nowx + x][nowy + y] != 1:
            continue

        if nowx + x == N and nowy + y == M:
            result = min(result, graph[nowx][nowy] + 1)
            break

        graph[nowx + x][nowy + y] = graph[nowx][nowy] + 1
        q.append((nowx + x, nowy + y))

print(result)