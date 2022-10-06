import collections
N, M = map(int, input().split())

q = collections.deque([])
graph = []
for i in range(M):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(len(line)):
        if line[j] == 1:
            q.append((i, j))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(result, q):
    while q:
        na, nb = q.popleft()

        for i, j in d:
            nx = na + i
            ny = nb + j

            if nx < 0 or nx >= M or ny < 0 or ny >= N or graph[nx][ny] != 0:
                continue

            graph[nx][ny] = graph[na][nb] + 1
            result = max(result, graph[nx][ny])
            q.append((nx, ny))

    return result if not result else result - 1

answer = bfs(0, q)

check = 0
for g in graph:
    if 0 in g:
        print(-1)
        check = 1
        break

if not check:
    print(answer)
