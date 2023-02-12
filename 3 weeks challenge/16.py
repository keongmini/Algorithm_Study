from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(N):          # 그래프 그리기
    new = list(map(int, input().split()))
    graph.append(new)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    tmp_graph = []
    for i in range(len(graph)):
        tmp_graph.append(graph[i][:])

    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx, ny))

    cnt = 0
    for i in range(N):
        cnt += tmp_graph[i].count(0)

    global result
    result = max(result, cnt)

def makewall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt + 1)
                graph[i][j] = 0

result = 0
makewall(0)
print(result)