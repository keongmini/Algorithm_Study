# bfs 이용한 풀이  -> 시간초과
# 모든 간선의 비용이 1일 때 -> bfs 사용
from collections import deque
n, m, k, x = map(int, input().split())

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True

    result = [0 for _ in range(n + 1)]
    while que:
        v = que.popleft()

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                result[i] = result[v] + 1

    for i in range(len(result)):
        if result[i] == k:
            print(i)

    if k not in result:
        print(-1)


graph = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

visited = [False] * (n + 1)

bfs(graph, x, visited)



# 책 풀이 보고 수정한 풀이
from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

que = deque([x])
result = [-1] * (n + 1)
result[x] = 0

while que:
    v = que.popleft()

    for i in graph[v]:
        if result[i] == -1:
            que.append(i)
            result[i] = result[v] + 1

check = False
for i in range(1, n + 1):
    if result[i] == k:
        print(i)
        check = True

if not check:
    print(-1)

