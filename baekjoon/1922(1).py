import heapq

N = int(input())
M = int(input())

q = []

for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


parent = [i for i in range(N + 1)]

result = 0

while q:
    c, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c

print(result)