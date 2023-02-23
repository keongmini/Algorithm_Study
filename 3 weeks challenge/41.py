N, M = map(int, input().split())


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


parent = [i for i in range(N + 1)]

for i in range(1, N + 1):
    new = list(map(int, input().split()))
    for n in range(1, N + 1):
        if new[n - 1] == 1:
            unionParent(parent, i, n)

nums = set(map(int, input().split()))

result = set()
for num in nums:
    now = getParent(parent, num)
    result.add(now)

if len(result) > 1:
    print('NO')
else:
    print('YES')





