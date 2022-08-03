from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x,y))   # 시작노드 삽입

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0, 0))

# 주의할점!!!
# 노드의 좌우상하를 확인하면서 조건에 맞을 때마다 해당 노드 + 1 값으로 바꿔주기 때문에
# 처음 시작 위치인 (0,0)의 인접노드에서 반복문을 돌다가 시작 노드를 1 -> 3으로 바꿔주는 문제가 발생할 수 있음
# 하지만 que에 다시 삽입된다 하더라도 시작 노드의 인접노드 중 1인 값이 더이상 없기 때문에 문제가 되지 않음
# 게다가 해당 문제는 마지막 위치의 값만 출력하면 되기 때문에 상관없음
