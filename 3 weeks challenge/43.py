import heapq


def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, x, y):
    x = getParent(parent, x)
    y = getParent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())

q = []
total = 0
for _ in range(M):
    X, Y, Z = map(int, input().split())
    total += Z
    heapq.heappush(q, (Z, X, Y))

parent = [i for i in range(N)]

result = 0
for _ in range(M):
    z, x, y = heapq.heappop(q)

    if getParent(parent, x) != getParent(parent, y):
        unionParent(parent, x, y)
        result += z

print(total - result)

