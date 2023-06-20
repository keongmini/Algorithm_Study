import collections

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = collections.defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n + 1)]

q = collections.deque()
q.append((a, 0))
visited[a] = True

result = -1

while q:
    now, path = q.popleft()

    if now == b:
        result = path
        break

    for i in graph[now]:
        if not visited[i]:
            q.append((i, path + 1))
            visited[i] = True

print(result)