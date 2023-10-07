# 크루스칼 알고리즘 풀이

def solution(n, costs):
    def get_parent(parent, x):
        if parent[x] != x:
            parent[x] = get_parent(parent, parent[x])

        return parent[x]

    def union_parent(parent, x, y):
        x = get_parent(parent, x)
        y = get_parent(parent, y)

        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    parent = [i for i in range(n + 1)]

    costs.sort(key=lambda x: x[2])

    result = 0

    for a, b, cost in costs:

        if get_parent(parent, a) != get_parent(parent, b):          # 주의! 그냥 parent의 값으로 비교하면 안됨 - 가장 최고 위치에 있는 parent의 값을 구해야하기 때문에
            union_parent(parent, a, b)
            result += cost

    return result

