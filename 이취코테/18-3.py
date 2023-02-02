import heapq

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())

parent = [i for i in range(N)]
result = 0

q = []
for _ in range(M):
    X, Y, Z = map(int, input().split())
    heapq.heappush(q, (Z, X, Y))
    result += Z

while q:
    a, b, c = heapq.heappop(q)

    if find(parent, b) != find(parent, c):
        union(parent, b, c)
        result -= a

print(result)
