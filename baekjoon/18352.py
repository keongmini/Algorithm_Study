import sys
import collections

input = sys.stdin.readline

# DFS 풀이 - 시간초과
# N, M, K, X = map(int, input().split())
#
# path = collections.defaultdict(list)
# for _ in range(M):
#     f, t = list(map(int, input().split()))
#     path[f].append(t)
#
# result = [1000001 for i in range(N + 1)]
#
# def dfs(a, cnt):
#     if not path[a]:
#         return
#
#     if cnt == K:
#         return
#
#     cnt += 1
#     for i in path[a]:
#         result[i] = min(result[i], cnt)
#         dfs(i, cnt)
#
#
# for i in path[X]:
#     result[i] = min(result[i], 1)
#     dfs(i, 1)
#
# if K not in result:
#     print(-1)
# else:
#     for r in range(len(result)):
#         if result[r] == K:
#             print(r)

# BFS 풀이 + sys - 통과
import sys
import collections

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

path = collections.defaultdict(list)
for _ in range(M):
    f, t = list(map(int, input().split()))
    path[f].append(t)

result = []
visited = [False for i in range(N + 1)]
visited[X] = True

q = collections.deque([[X, 0]])
while q:
    now, cnt = q.popleft()

    if cnt == K:
        result.append(now)
        continue

    for n in path[now]:
        if not visited[n]:
            visited[n] = True
            q.append([n, cnt + 1])

if not result:
    print(-1)
else:
    result.sort()
    for r in result:
        print(r)

