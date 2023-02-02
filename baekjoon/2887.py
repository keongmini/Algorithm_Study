import heapq
import sys

input = sys.stdin.readline

N = int(input())

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if parent[a] < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N)]

xyz = [[] for _ in range(3)]
for i in range(N):
    x, y, z = map(int, input().split())
    xyz[0].append((x, i))
    xyz[1].append((y, i))
    xyz[2].append((z, i))

for i in range(3):
    xyz[i].sort()

q = []
for i in range(3):
    for j in range(1, N):
        d1, a = xyz[i][j - 1]
        d2, b = xyz[i][j]
        heapq.heappush(q, (abs(d1 - d2), a, b))

cnt = N - 1
result = 0

while cnt > 0:
    d, a, b = heapq.heappop(q)

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += d
        cnt -= 1

print(result)