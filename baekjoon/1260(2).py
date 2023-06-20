import collections

N, M, V = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

for i in graph.keys():
    graph[i].sort()


def dfs(k, visited, result):
    visited[k] = True
    result.append(k)

    for i in graph[k]:
        if not visited[i]:
            dfs(i, visited, result)


visited = [False for _ in range(N + 1)]
result = []
dfs(V, visited, result)

for r in result:
    print(r, end=" ")

print()


def bfs(k, visited, result):
    q = collections.deque([k])
    visited[k] = True

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


visited = [False for _ in range(N + 1)]
result = []
bfs(V, visited, result)

for r in result:
    print(r, end=" ")
