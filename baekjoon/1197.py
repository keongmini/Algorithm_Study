import heapq
n, m = map(int, input().split())
q = []

for _ in range(m):
    a, b, w = map(int, input().split())
    heapq.heappush(q, (w, a, b))

parent = [i for i in range(n + 1)]

def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
while q:
    w, a, b = heapq.heappop(q)

    if getParent(parent, a) != getParent(parent, b):
        unionParent(parent, a, b)
        result += w

print(result)