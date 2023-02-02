N, M = map(int, input().split())

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

parent = [i for i in range(N + 1)]

for i in range(N):
    new = list(map(int, input().split()))
    for j in range(N):
        if new[j] == 1:
            union(parent, i + 1, j + 1)

destination = list(map(int, input().split()))
destination = list(set(destination))

flag = 0
for i in range(len(destination) - 1):
    if find(parent, destination[i]) != find(parent, destination[i + 1]):
        print("NO")
        flag = 1
        break

if not flag:
    print("YES")


