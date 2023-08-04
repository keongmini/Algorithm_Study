from collections import defaultdict, deque

N = int(input())

check = defaultdict(list)

graph = []

for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

    for j in range(N):
        check[graph[i][j]].append((i, j))

nums = list(check.keys())
nums.sort()

result = 1

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    now = 0

    q = deque()
    visited = [[False for _ in range(N)] for z in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] != -1 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for a, b in move:
                        nx = x + a
                        ny = y + b

                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue

                        if graph[nx][ny] == -1 or visited[nx][ny]:
                            continue

                        q.append((nx, ny))
                        visited[nx][ny] = True
                now += 1

    return now


for num in nums:
    for x, y in check[num]:
        graph[x][y] = -1

    result = max(result, bfs())

print(result)


