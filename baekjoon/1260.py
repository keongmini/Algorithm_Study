import collections

N, M, V = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(M):
    m, n = map(int, input().split())
    graph[m].append(n)
    graph[n].append(m)

for i in graph.keys():                  # 정렬 해줘야함
    graph[i].sort()

visited = [False] * (N + 1)

result = []

def dfs(k, visited, result):
    visited[k] = True
    result.append(k)

    for i in graph[k]:
        if not visited[i]:
            dfs(i, visited, result)

dfs(V, visited, result)

visited = [False] * (N + 1)

answer = []

def bfs(k, visited, answer):
    q = collections.deque([k])
    visited[k] = True

    while q:
        now = q.popleft()
        answer.append(now)

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

bfs(V, visited, answer)

for i in result:
    print(i, end=" ")
print()
for i in answer:
    print(i, end=" ")
