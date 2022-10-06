import collections
import sys

sys.setrecursionlimit(5000)         # dfs 풀이를 위해 필요
input = sys.stdin.readline

N, M = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(M):
    i, n = map(int, input().split())
    graph[i].append(n)
    graph[n].append(i)

visited = [False] * (N + 1)

def bfs(k, visited):
    q = collections.deque([k])
    visited[k] = True

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def dfs(k, visited):
    visited[k] = True

    for i in graph[k]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited)

    return

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i, visited)
            cnt += 1

print(cnt)