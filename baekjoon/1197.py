import heapq
n, m = map(int, input().split())
q = []

for _ in range(m):
    a, b, w = map(int, input().split())
    heapq.heappush(q, (w, a, b))        # 가중치를 기준으로 정렬

parent = [i for i in range(n + 1)]

# 유니온 파인드 구현 - 해당 문제에서 파인드 제외
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

    if getParent(parent, a) != getParent(parent, b):        #  부모 노드 찾기 / 같을 경우 사이클
        unionParent(parent, a, b)       # Union
        result += w

print(result)