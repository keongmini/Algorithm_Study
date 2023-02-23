from collections import deque

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

T = int(input())

for _ in range(T):
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    changed = []
    for _ in range(m):
        new = list(map(int, input().split()))
        changed.append(new)

    upper = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            upper[t[j]].append(t[i])

    for x, y in changed:
        if x in upper[y]:
            upper[x].append(y)
            upper[y].remove(x)
        else:
            upper[y].append(x)
            upper[x].remove(y)

    result = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        result[len(upper[i])] = i

    result = result[:-1]

    if result.count(0) > 1:
        certain = True
        parent = [i for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in upper[i]:
                if getParent(parent, i) != getParent(parent, j):
                    unionParent(parent, i, j)
                else:
                    print('IMPOSSIBLE')
                    certain = False
                    break

            if not certain:
                break
        if certain:
            print("?")
    else:
        for r in result:
            print(r, end=" ")