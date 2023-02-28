import heapq


def get(parent, x):
    if parent[x] == x:
        return x
    parent[x] = get(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = get(parent, x)
    y = get(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def solution(n, costs):
    q = []

    for start, to, cost in costs:
        heapq.heappush(q, (cost, start, to))

    parent = [i for i in range(n)]

    result = 0
    while q:
        cost, start, to = heapq.heappop(q)

        if get(parent, start) == get(parent, to):
            continue

        union(parent, start, to)
        result += cost

    return result

