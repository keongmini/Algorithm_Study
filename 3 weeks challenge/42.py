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

G = int(input())
P = int(input())

info = [int(input()) for _ in range(P)]

parent = [i for i in range(G + 1)]

result = 0

for i in info:
    now = getParent(parent, i)
    if now == 0:
        break
    unionParent(parent, now, now - 1)
    result += 1

print(result)