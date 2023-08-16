from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])

result = [0 for _ in range(N + 1)]
result[1] = 1

while q:
    now = q.popleft()

    for n in graph[now]:
        if result[n] == 0:
            result[n] = now
            q.append(n)

for i in range(2, N + 1):
    print(result[i])