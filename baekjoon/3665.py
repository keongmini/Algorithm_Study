import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())


def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


for _ in range(T):
    n = int(input())
    ti = list(map(int, input().split()))
    m = int(input())

    indegree = defaultdict(set)

    for i in range(len(ti)):
        for j in range(i + 1, len(ti)):
            indegree[ti[j]].add(ti[i])

    indegree[ti[0]]

    # ---------------------- 입력값 정리

    inputs = []
    for _ in range(m):
        n1, n2 = map(int, input().split())
        inputs.append((n1, n2))

    for n1, n2 in inputs:
        if n2 in indegree[n1]:
            indegree[n2].add(n1)
            indegree[n1].remove(n2)
        elif n1 in indegree[n2]:
            indegree[n1].add(n2)
            indegree[n2].remove(n1)

    result = [0 for _ in range(n)]
    for k in indegree.keys():
        result[len(indegree[k])] = k

    parent = [i for i in range(n + 1)]
    if result.count(0) > 1:
        check = True
        for i in indegree.keys():
            for j in indegree[i]:
                if find(parent, i) != find(parent, j):
                    union(parent, i, j)
                else:
                    print('IMPOSSIBLE')
                    check = False
                    break
            if not check:
                break
        if check:
            print("?")
    else:
        for r in result:
            print(r, end=" ")