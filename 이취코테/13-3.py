# 내 풀이
from collections import deque

n, k = map(int, input().split())

graph = []
data = deque()

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]:
            data.append([graph[i][j], i, j])

s, a, b = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

time = 0
cnt = 0
while data and time < s:
    now = data.popleft()
    cnt += 1

    for i in range(4):
        x = now[1] + dx[i]
        y = now[2] + dy[i]

        if x < 0 or x >= n or y < 0 or y >= n:
            continue

        if not graph[x][y]:
            graph[x][y] = now[0]
            data.append([graph[x][y], x, y])

    if cnt == k:
        time += 1
        cnt = 0

print(graph[a - 1][b - 1])


# 개선 풀이
# 처음 들어올 때 낮은 숫자부터 들어오지 않을 경우도 고려해주어야 함!
from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j, 0))

data.sort()
q = deque(data)

s, a, b = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    now = q.popleft()

    if now[3] == s:
        break

    for i in range(4):
        x = now[1] + dx[i]
        y = now[2] + dy[i]

        if x < 0 or x >= n or y < 0 or y >= n:
            continue

        if not graph[x][y]:
            graph[x][y] = now[0]
            q.append([graph[x][y], x, y, now[3] + 1])

print(graph[a - 1][b - 1])



