# 크루스칼 알고리즘(MST): 간선에 가중치가 다를 때, 가중치의 합이 최소가 되는 신장트리 알고리즘
# 다익스트라 알고리즘: 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단경로 알고리즘

# 최소 비용 구하기 => 크루스칼 알고리즘

import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

q = []
for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))                # 가중치 작은 순서대로 확인하도록 힙 사용


def find_parent(parent, x):
    if parent[x] != x:
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

    if find_parent(parent, a) != find_parent(parent, b):        # 사이클인지 = 이미 확인된 간선 정보인지 - 가중치 작은 순서대로 확인하기 때문에 이미 확인했으면 확인할 필요 x
        union_parent(parent, a, b)
        result += c

print(result)